from typing import List
import itertools

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        evens = set()
        # 3桁の順列をすべて生成
        for p in itertools.permutations(digits, 3):
            if p[0] == 0:
                continue
            val = p[0] * 100 + p[1] * 10 + p[2]
            if val % 2 == 0:
                evens.add(val)
        return len(evens)

