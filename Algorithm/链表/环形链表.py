from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            ##slow和fast需要先更新，因为如果只有两个元素的话会出现说fast.next没有数的情况
            slow=slow.next
            fast=fast.next.next
            ##最后我们的slow找到的是两个快慢指针环的相遇点，而不是环的入口
            if slow is fast:
                return True

        return False