# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
            
        dummy = ListNode(0, head)
        prev = dummy
        
        # prevポインタを反転対象の直前（left - 1）の位置まで進める
        for _ in range(left - 1):
            prev = prev.next
            
        # currは反転前の範囲で先頭にあるノード（反転後はこの部分範囲の末尾になる）
        curr = prev.next
        
        # right - left 回、currの次のノードを prev の直後に移動する（前挿入）
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
            
        return dummy.next

