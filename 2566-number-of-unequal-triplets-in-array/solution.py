from typing import List
from collections import Counter

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ans = 0
        prev = 0
        total = len(nums)
        
        # 各ユニーク要素を中央の値として選ぶ組み合わせを数える
        for val, curr in counts.items():
            next_ = total - prev - curr
            ans += prev * curr * next_
            prev += curr
            
        return ans

