# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        rst = []

        def util(root):
            if root:
                util(root.left)
                rst.append(root.val)
                util(root.right)

        util(root)
        return rst
