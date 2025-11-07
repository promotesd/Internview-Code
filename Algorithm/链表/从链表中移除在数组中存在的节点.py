from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set(nums)
        cur=dummy=head
        i=0
        l=len(s)
        while cur.next:
            if cur.next.val in s:
                cur.next=cur.next.next
            else:
                