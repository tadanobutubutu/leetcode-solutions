class Solution:
    def sumRootToLeaf(self, root):
        def dfs(node, cur):
            if not node:
                return 0

            cur = (cur << 1) | node.val

            if not node.left and not node.right:
                return cur

            return dfs(node.left, cur) + dfs(node.right, cur)

        return dfs(root, 0)

