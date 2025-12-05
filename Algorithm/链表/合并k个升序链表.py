from typing import List
from typing import Optional
from heapq import heapify, heappop, heappush

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ListNode.__lt__=lambda a, b : a.val< b.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        cur=dummy=ListNode()
        h=[head for head in lists if head]
        heapify(h)

        while h:
            node=heappop(h)
            if node.next:
                heappush(h,node.next)

            cur.next=node
            cur=cur.next
        return dummy.next
            