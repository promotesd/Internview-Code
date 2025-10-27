from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def mergeNodes(self, head:Optional[ListNode])->Optional[ListNode]:
        tail=head
        cur=head.next
        while cur.next:
            if cur.val!=0:
                tail.val+=cur.val
            else:
                tail=tail.next
                tail.val=0
            cur=cur.next
        tail.next=None
        return head
