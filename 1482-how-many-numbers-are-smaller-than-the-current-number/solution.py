from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Create a sorted copy of the array
        sorted_nums = sorted(nums)
        # Map each number to the index of its first occurrence
        mapping = {}
        for idx, val in enumerate(sorted_nums):
            if val not in mapping:
                mapping[val] = idx
        # Map the original numbers to their respective counts
        return [mapping[x] for x in nums]

