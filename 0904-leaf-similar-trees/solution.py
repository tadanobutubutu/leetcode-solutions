class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(node):
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
            else:
                yield from leaves(node.left)
                yield from leaves(node.right)

        return list(leaves(root1)) == list(leaves(root2))

