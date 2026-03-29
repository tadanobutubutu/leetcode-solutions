# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        
        def dfs(node, path):
            if not node:
                return
            # 現在のノードをパスに追加
            path += str(node.val)
            # 葉ノードなら結果に追加
            if not node.left and not node.right:
                res.append(path)
            else:
                path += "->"
                dfs(node.left, path)
                dfs(node.right, path)
        
        dfs(root, "")
        return res

