import json 
import os 
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Sequence, Tuple

import regex as re

_DEFAULT_PATTERN=r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
_PRETOKENIZER=re.compile(_DEFAULT_PATTERN)

def _pre_tokenize(text:str)->List[str]:
    return [m.group(0) for m in _PRETOKENIZER.finditer(text)]

def _bytes_split(tok:str)->List[bytes]:
    b=tok.encode("utf-8")
    return [b[i:i+1] for i in range(len(b))]

class Tokenizer:
    def __init__(
        self,
        vocab:Dict[int,bytes],
        merges:List[Tuple[bytes,bytes]],
        special_tokens:List[str]|None=None,
    ):
        self.id2tok:Dict[int, bytes]=dict(vocab)
        self.tok2id:Dict[bytes, int]={v:k for k,v in vocab.items()}

        self.special_tokens:List[str]=special_tokens or []

        for s in self.special_tokens:
            b=s.encode("utf-8")
            if b not in self.id2tok:
                new_id=max(self.id2tok)+1
                self.id2tok[new_id]=b
                self.tok2id[b]=new_id
        if self.special_tokens:
            esc=[re.escape(st) for st in sorted(self.special_tokens, key=len,reverse=True)]
            self._special_re=re.compile("|".join(esc))
        else:
            self._specia_re=None

        self.merge_rank:Dict[Tuple[bytes,bytes],int]={
            pair:r for r,pair in enumerate(merges)
        }
    
    @classmethod
    def from_files(
        cls,
        vocab_filepath:str|os.PathLike,
        merges_filepath:str|os.PathLike,
        special_tokens:List[str]|None=None
    )->"Tokenizer":
        with Path(vocab_filepath).open() as vf:
            raw_vocab=json.load(vf)
        vocab={int(i):k.encode('utf-8') for k,i in raw_vocab.items()}

        merges:List[Tuple[bytes,bytes]]=[]
        with Path(merges_filepath).open() as mf:
            for line in mf:
                parts=line.strip().split()
                if len(parts)==2:
                    merges.append((parts[0],parts[1]))
        return cls(vocab,merges,special_tokens)
    
    def _bpe(self,token:str) -> List[int]:
        b_token=token.encode("utf-8")
        if b_token in self.tok2id:
            return [self.tok2id[b_token]]
        seq:List[bytes]= _bytes_split(token)
        if len(seq)==1:
            return [self.tok2id[seq[0]]]
        
        while True:
            best_rank=None
            best_idx=None
            for i in range(len(seq)-1):
                pair=(seq[i],seq[i+1])
                rank=self.merge_rank.get(pair)
                if rank is None:
                    continue
                if best_rank is None or rank<best_rank:
                    best_rank=rank
                    best_idx=i
            
            if best_idx is None:
                break

            seq[best_idx:best_idx+2]=[seq[best_idx]+seq[best_idx+1]]
        return [self.tok2id[b] for b in seq]
    

    def _split_with_special(self,text:str)->Iterator[Tuple[str,str]]:
        if not self._special_re:
            yield ("text",text)
            return 
        pos=0
        for m in self._special_re.finditer(text):
            if m.start()>pos:
                yield ("text",text[pos:m.start()])
            yield("special", m.group(0))
            pos=m.end()
        
        if pos<len(text):
            yield("text",text[pos:])


    def encode(self,text:str)->List[int]:
        ids:List[int]=[]
        for kind, chunk in self._split_with_special(text):
            if not chunk:
                continue
            if kind =="special":
                ids.append(self.tok2id[chunk.encode("utf-8")])
            else:
                for tok in _pre_tokenize(chunk):
                    ids.extend(self._bpe(tok))
        return ids

    def encode_iterabel(self,iterable:Iterable[str])->Iterable[int]:
        for chunk in iterable:
            for tid in self.encode(chunk):
                yield tid

    def decode(self,ids:Sequence[int])->str:
        return b"".join(self.id2tok[i] for i in ids).decode("utf-8",errors="replace")
