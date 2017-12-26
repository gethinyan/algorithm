"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        leftTree = self.postorderTraversal(root.left)
        rightTree = self.postorderTraversal(root.right)
        return leftTree + rightTree + [root.val]
