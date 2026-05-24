from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        # first を n + 1 歩進める
        for _ in range(n + 1):
            first = first.next
            
        # first が末尾に到達するまで両方を進める
        while first is not None:
            first = first.next
            second = second.next
            
        # second.next が削除対象のノードなので、それをスキップする
        second.next = second.next.next
        
        return dummy.next

