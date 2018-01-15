"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        lDepth = self.getDepth(root.left)
        rDepth = self.getDepth(root.right)
        diff = lDepth - rDepth
        if diff < -1 or diff > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, Root):
        if Root is None:
            return 0
        lDepth = self.getDepth(Root.left)
        rDepth = self.getDepth(Root.right)
        return max(lDepth, rDepth) + 1
