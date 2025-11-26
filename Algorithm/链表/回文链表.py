from typing import Optional, Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:


    def middleNode(self, head: Optional[ListNode])->Tuple[Optional[ListNode], Optional[ListNode]]:
        pre=None
        slow=fast=head
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next.next
        return pre, slow

    def reverseList(self, head:Optional[ListNode])-> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt

        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True

        isPal=True

        pre, mid=self.middleNode(head)

        head2=self.reverseList(mid)
        while head2:
            if head.val!=head2.val:
                isPal=False
                break
            head=head.next
            head2=head2.next
        
        return isPal
