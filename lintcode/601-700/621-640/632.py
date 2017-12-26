class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """

    def maxNode(self, root):
        # write your code here
        if root is None:
            return None
        leftNode = self.maxNode(root.left)
        rightNode = self.maxNode(root.right)
        if (leftNode is not None and leftNode.val > root.val):
            root = leftNode
        if (rightNode is not None and rightNode.val > root.val):
            root = rightNode
        return root
