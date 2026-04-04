class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            # 直径候補を更新（辺の数なので left + right）
            self.ans = max(self.ans, left + right)

            # このノードの高さを返す
            return 1 + max(left, right)

        depth(root)
        return self.ans

