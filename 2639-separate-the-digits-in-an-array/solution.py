from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            for char in str(x):
                ans.append(int(char))
        return ans

