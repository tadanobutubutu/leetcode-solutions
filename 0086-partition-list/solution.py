# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # x未満の要素を集めるためのリストのダミーヘッド
        before_head = ListNode(0)
        before = before_head
        
        # x以上の要素を集めるためのリストのダミーヘッド
        after_head = ListNode(0)
        after = after_head
        
        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next
            
        # リストの末尾をNoneにして循環参照を防ぐ
        after.next = None
        
        # 2つのリストを連結する
        before.next = after_head.next
        
        return before_head.next

