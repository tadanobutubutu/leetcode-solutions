from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_k = -1
        for x in nums:
            # 正の数であり、かつその負数がセット内に存在する場合
            if x > 0 and -x in num_set:
                max_k = max(max_k, x)
        return max_k

