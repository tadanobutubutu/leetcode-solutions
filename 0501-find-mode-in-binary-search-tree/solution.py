# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None
        self.count = 0
        self.max_count = 0
        self.modes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # Count logic
            if self.prev is None or self.prev != node.val:
                self.count = 1
            else:
                self.count += 1

            # Update modes
            if self.count > self.max_count:
                self.max_count = self.count
                self.modes = [node.val]
            elif self.count == self.max_count:
                self.modes.append(node.val)

            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.modes

