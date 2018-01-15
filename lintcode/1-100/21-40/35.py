"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        # write your code here
        if head is None:
            return
        result = ListNode(head.val)
        head = head.next
        while head is not None:
            tmpNode = ListNode(head.val)
            tmpNode.next = result
            result = tmpNode
            head = head.next

        return result
