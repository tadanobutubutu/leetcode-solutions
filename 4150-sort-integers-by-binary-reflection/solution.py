from typing import List

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def get_reflection(x: int) -> int:
            return int(bin(x)[2:][::-1], 2)
            
        nums.sort(key=lambda x: (get_reflection(x), x))
        return nums

