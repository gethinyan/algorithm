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
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        result = []
        currentList = []
        nextList = []
        level = []
        if root is None:
            return []
        currentList.append(root)
        while len(currentList) != 0:
            while len(currentList) != 0:
                node = currentList.pop(0)
                level.append(node.val)
                if node.left is not None:
                    nextList.append(node.left)
                if node.right is not None:
                    nextList.append(node.right)
            currentList, nextList = nextList, []
            result.append(level)
            level = []
        return result
