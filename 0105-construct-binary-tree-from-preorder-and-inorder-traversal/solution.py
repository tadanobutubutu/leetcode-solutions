# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0
        
        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if in_left > in_right:
                return None
                
            val = preorder[pre_idx]
            root = TreeNode(val)
            pre_idx += 1
            
            index = inorder_map[val]
            
            # 先行順（Root -> Left -> Right）なので、左サブツリー、次に右サブツリーの順で再帰構築する
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)
            
            return root
            
        return helper(0, len(inorder) - 1)

