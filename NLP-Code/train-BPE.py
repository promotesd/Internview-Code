# -*- coding: utf-8 -*-

from __future__ import annotations

import multiprocessing as mp
import os
import regex as re
from collections import Counter, defaultdict
from pathlib import Path
from typing import BinaryIO, Dict, List, Tuple



_DEFAULT_PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
_PRETOKENIZER = re.compile(_DEFAULT_PAT)


def _find_chunk_boundaries(f: BinaryIO, n_chunks: int, delim: bytes) -> List[int]:
    """把文件粗分 n_chunks 段，再向后对齐到 special token 开头。"""
    f.seek(0, os.SEEK_END)
    size = f.tell()
    base = size // n_chunks
    bounds = [i * base for i in range(n_chunks)] + [size]

    mini = 4096
    for i in range(1, n_chunks):
        pos = bounds[i]
        f.seek(pos)
        while True:
            buf = f.read(mini)
            if not buf:
                bounds[i] = size
                break
            j = buf.find(delim)
            if j != -1:
                bounds[i] = pos + j
                break
            pos += mini
    return sorted(set(bounds))


def _split_on_special(text: str, specials: List[str]) -> List[str]:
    pattern = "|".join(re.escape(tok) for tok in specials)
    return [p for p in re.split(f"({pattern})", text) if p]


def _pre_tokenize(text: str, pattern=_PRETOKENIZER) -> List[str]:
    return [m.group(0) for m in pattern.finditer(text)]


def _pretokenize_chunk(args) -> Counter:
    start, end, path, specials = args
    with open(path, "rb") as f:
        f.seek(start)
        chunk = f.read(end - start).decode("utf-8", errors="ignore")
    chunk = chunk.replace("\r\n", "\n").replace("\r", "\n")

    cnt = Counter()
    for seg in _split_on_special(chunk, specials):
        if seg in specials:
            continue
        cnt.update(_pre_tokenize(seg))
    return cnt


def _parallel_pre_tokenize(
    input_path: str | os.PathLike,
    special_tokens: List[str],
    n_proc: int | None = None,
) -> Counter:
    n_proc = n_proc or mp.cpu_count()
    with open(input_path, "rb") as f:
        bounds = _find_chunk_boundaries(f, n_proc, special_tokens[0].encode())
    tasks = [(s, e, str(input_path), special_tokens) for s, e in zip(bounds[:-1], bounds[1:])]

    with mp.Pool(n_proc) as pool:
        total = Counter()
        for part in pool.imap_unordered(_pretokenize_chunk, tasks):
            total.update(part)
    return total



def train_bpe(
    input_path: str | os.PathLike,
    vocab_size: int,
    special_tokens: List[str],
    num_processes: int | None = None,
) -> Tuple[Dict[int, bytes], List[Tuple[bytes, bytes]]]:

    # ---------- 1. 并行预分词 ----------
    str_counts = _parallel_pre_tokenize(input_path, special_tokens, num_processes)

    # ---------- 2. 构建 word_counts ----------
    word_counts: Counter[Tuple[bytes, ...]] = Counter()
    for tok, freq in str_counts.items():
        b = tok.encode("utf-8")
        word_counts[tuple(b[i : i + 1] for i in range(len(b)))] += freq

    # ---------- 3. 初始化词表 ----------
    min_vocab = 256 + len(special_tokens)
    if vocab_size < min_vocab:
        raise ValueError(f"vocab_size must be ≥ {min_vocab}")

    id2token: Dict[int, bytes] = {i: bytes([i]) for i in range(256)}
    next_id = 256
    for tok in special_tokens:
        id2token[next_id] = tok.encode("utf-8")
        next_id += 1

    merges: List[Tuple[bytes, bytes]] = []

    # ---------- 4. 初始 pair 计数与倒排 ----------
    pair_counts: Counter[Tuple[bytes, bytes]] = Counter()
    pair_to_seqs: Dict[Tuple[bytes, bytes], set[Tuple[bytes, ...]]] = defaultdict(set)

    for seq, freq in word_counts.items():
        for i in range(len(seq) - 1):
            p = (seq[i], seq[i + 1])
            pair_counts[p] += freq
            pair_to_seqs[p].add(seq)

    # ---------- 5. 迭代合并 ----------
    while next_id < vocab_size and pair_counts:
        # 5.1 选最优 pair（频次高→字典序大）
        best_pair, _ = max(pair_counts.items(), key=lambda kv: (kv[1], kv[0]))
        merges.append(best_pair)

        new_token = best_pair[0] + best_pair[1]
        id2token[next_id] = new_token
        next_id += 1

        # 5.2 找所有受影响序列
        affected = pair_to_seqs.pop(best_pair)
        if not affected:
            continue

        # 5.3 更新 word_counts / pair_counts / 倒排
        for seq in affected:
            freq = word_counts.pop(seq)
            # 删除旧 pair 统计
            for i in range(len(seq) - 1):
                p = (seq[i], seq[i + 1])
                pair_counts[p] -= freq
                if pair_counts[p] <= 0:
                    pair_counts.pop(p, None)
                pair_to_seqs[p].discard(seq)

            # 合并 seq
            merged: list[bytes] = []
            i = 0
            while i < len(seq):
                if i < len(seq) - 1 and seq[i] == best_pair[0] and seq[i + 1] == best_pair[1]:
                    merged.append(new_token)
                    i += 2
                else:
                    merged.append(seq[i])
                    i += 1
            merged_seq = tuple(merged)
            word_counts[merged_seq] += freq

            # 加入新 pair 统计
            for i in range(len(merged_seq) - 1):
                p = (merged_seq[i], merged_seq[i + 1])
                pair_counts[p] += freq
                pair_to_seqs[p].add(merged_seq)

    return id2token, merges



# if __name__ == "__main__":
#     import argparse, json, time, pickle

#     pa = argparse.ArgumentParser(description="Train byte-level BPE tokenizer")
#     pa.add_argument("input", type=Path)
#     pa.add_argument("--vocab_size", type=int, default=1000)
#     pa.add_argument("--special", nargs="*", default=["<|endoftext|>"])
#     pa.add_argument("--out_dir", type=Path, default=Path("./bpe_out"))
#     args = pa.parse_args()

#     t0 = time.time()
#     vocab, merges = train_bpe(args.input, args.vocab_size, args.special)
#     dt = time.time() - t0
#     print(f" done in {dt:.2f}s — vocab={len(vocab)}, merges={len(merges)}")

#     args.out_dir.mkdir(parents=True, exist_ok=True)
#     with open(args.out_dir / "vocab.json", "w") as f:
#         json.dump({i: v.decode("latin1") for i, v in vocab.items()}, f)
#     with open(args.out_dir / "merges.pkl", "wb") as f:
#         pickle.dump(merges, f)
#     print(f"saved to {args.out_dir}")
