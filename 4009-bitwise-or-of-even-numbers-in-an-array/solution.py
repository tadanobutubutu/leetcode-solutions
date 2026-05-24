from typing import List
from functools import reduce
import operator

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        even_nums = [x for x in nums if x % 2 == 0]
        if not even_nums:
            return 0
        return reduce(operator.or_, even_nums)

