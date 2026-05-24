from collections import Counter

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        counts = Counter(nums)
        for num in nums:
            if num % 2 == 0 and counts[num] == 1:
                return num
        return -1

