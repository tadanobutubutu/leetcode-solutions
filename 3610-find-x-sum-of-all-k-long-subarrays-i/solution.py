from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n - k + 1):
            sub = nums[i : i + k]
            counts = Counter(sub)
            
            # (頻度, 値) の降順でソート
            sorted_items = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=True)
            
            # 上位 x 個のみを取り出して和を計算
            top_x = sorted_items[:x]
            sub_x_sum = sum(val * freq for val, freq in top_x)
            ans.append(sub_x_sum)
            
        return ans

