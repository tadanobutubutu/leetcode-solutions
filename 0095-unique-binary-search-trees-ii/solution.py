# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
            
        # メモ化用の辞書
        memo = {}
        
        def generate(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]
                
            all_trees = []
            # startからendまでのすべての数iをルートとして試す
            for i in range(start, end + 1):
                # iの左側に位置する値 [start, i - 1] で構成されるすべての左部分木を生成
                left_trees = generate(start, i - 1)
                # iの右側に位置する値 [i + 1, end] で構成されるすべての右部分木を生成
                right_trees = generate(i + 1, end)
                
                # 左部分木と右部分木のすべての組み合わせにiをルートノードとして結合
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
                        
            memo[(start, end)] = all_trees
            return all_trees
            
        return generate(1, n)

