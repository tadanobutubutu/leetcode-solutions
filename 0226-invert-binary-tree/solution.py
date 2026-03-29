# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        # 左右を入れ替える
        root.left, root.right = root.right, root.left
        # 再帰的に反転
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

