# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 先頭にダミーノードを作成し、headの削除処理を容易にする
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            # 隣り合うノードの値が同じ場合、重複が発生している
            if prev.next.val == prev.next.next.val:
                val = prev.next.val
                # その値と等しいノードをすべてスキップする
                while prev.next and prev.next.val == val:
                    prev.next = prev.next.next
            else:
                # 重複がない場合は、通常通りポインタを進める
                prev = prev.next
                
        return dummy.next

