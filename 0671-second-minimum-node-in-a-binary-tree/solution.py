class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        smallest = root.val
        self.ans = float('inf')

        def dfs(node):
            if not node:
                return
            # root.val と異なる値を見つけたら候補
            if smallest < node.val < self.ans:
                self.ans = node.val
            # 同じ値なら子を探索
            elif node.val == smallest:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1

