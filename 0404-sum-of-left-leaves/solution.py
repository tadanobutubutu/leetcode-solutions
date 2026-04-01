class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, is_left):
            if not node:
                return 0
            # 左葉なら値を返す
            if not node.left and not node.right and is_left:
                return node.val
            # 左右の子を探索
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)

