class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node
                yield from inorder(node.right)

        dummy = TreeNode(0)
        cur = dummy

        for node in inorder(root):
            node.left = None
            cur.right = node
            cur = node

        return dummy.right

