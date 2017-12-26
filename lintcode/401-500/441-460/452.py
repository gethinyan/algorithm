"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """

    def removeElements(self, head, val):
        # write your code here
        cpHead = head
        if cpHead is None:
            return cpHead
        while cpHead.next is not None:
            if cpHead.next.val == val:
                cpHead.next = cpHead.next.next
            else:
                cpHead = cpHead.next
        if head.val == val:
            return head.next
        return head
