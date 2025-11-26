from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p,q = headA, headB
        while p is not q:
            ##为什么p和q不能是p.next is None,
            ##我们要让他在均为None的时候停下来，否则会不断循环
            p=p.next if p else headB
            q=q.next if q else headA
        return p
        