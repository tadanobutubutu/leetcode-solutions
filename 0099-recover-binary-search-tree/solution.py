# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = second = prev = None
        curr = root
        
        while curr:
            if not curr.left:
                # 訪問処理
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                # 前駆ノード（predecessor）を見つける
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if not pred.right:
                    # スレッドを張る
                    pred.right = curr
                    curr = curr.left
                else:
                    # スレッドを外して訪問処理
                    pred.right = None
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right
                    
        # 誤って入れ替えられた2つのノードの値をスワップ
        if first and second:
            first.val, second.val = second.val, first.val

