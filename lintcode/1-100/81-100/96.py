"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """

    def partition(self, head, x):
        # write your code here
        result = ListNode(0)
        result.next = head
        while result.next is not None and result.next.val < x:
            result = result.next
        tmp = result
        while tmp.next is not None:
            if tmp.next.val < x:
                node = ListNode(tmp.next.val)
                node.next = result.next
                result.next = node
                tmp.next = tmp.next.next
            tmp = tmp.next

        return head
