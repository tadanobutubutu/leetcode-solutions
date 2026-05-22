from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total_sum = sum(nums)
        subseq = []
        subseq_sum = 0
        for num in nums:
            subseq.append(num)
            subseq_sum += num
            if subseq_sum * 2 > total_sum:
                break
        return subseq

