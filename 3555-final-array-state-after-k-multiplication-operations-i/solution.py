import heapq
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # (値, インデックス)のタプルで最小ヒープを作成
        # 値が同じ場合はインデックスが小さいものが優先される
        heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(heap)
        
        for _ in range(k):
            val, idx = heapq.heappop(heap)
            new_val = val * multiplier
            nums[idx] = new_val
            heapq.heappush(heap, (new_val, idx))
            
        return nums

