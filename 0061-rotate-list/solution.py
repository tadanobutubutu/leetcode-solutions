from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
            
        # 1. リストの長さを測る & 末尾ノードを見つける
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # 2. 実質的な回転回数を計算
        k %= length
        if k == 0:
            return head
            
        # 3. リストを環状にする
        tail.next = head
        
        # 4. 新しい末尾ノード (new_tail) の位置まで進む
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # 5. 新しい先頭 (new_head) を設定し、環を切り離す
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head

