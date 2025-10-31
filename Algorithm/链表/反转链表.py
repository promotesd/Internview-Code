from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next


class Solution:
    def reverseList(self, head:Optional[ListNode])->Optional[ListNode]:
        '''
        递归解法
        '''
        if head is None or head.next is None:
            return head
        
        ##将head"递"到链表的最后一个节点
        rev_head=self.reverseList(head.next)
        ##”归“head到最后一个，return 最后一个head，，tail就是head的下一个就是none
        tail=head.next
        ##tail指向head
        tail.next=head
        ##反之出现环，否则如果是1->2->3.在遍历到2的时候，2.next=none，而不是3.
        head.next=None
        return rev_head

