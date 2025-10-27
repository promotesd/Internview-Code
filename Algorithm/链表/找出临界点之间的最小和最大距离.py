from typing import List, Optional
from math import inf

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def nodesBetweenCriticalPoints(self, head:Optional[ListNode])->List[int]:
        a,b,c=head, head.next, head.next.next
        minDis, first, last= inf, 0 , 0
        i=1
        while c:
            if a.val<b.val>c.val or a.val>b.val<c.val:
                if first==0:
                    first=i
                if i-last<minDis and last>0:
                    minDis=i-last
                last=i
            a,b,c,i=b,c,c.next,i+1
        return [minDis, last-first] if last!=first else [-1,-1]

