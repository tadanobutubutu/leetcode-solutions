from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next is not None and prev.next.next is not None:
            first = prev.next
            second = prev.next.next
            
            # ポインタの繋ぎ替え
            first.next = second.next
            second.next = first
            prev.next = second
            
            # 次のペアの直前に prev を進める
            prev = first
            
        return dummy.next

