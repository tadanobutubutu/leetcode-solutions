from typing import List

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        s = str(n)
        length = len(s)
        ans = []
        for i, char in enumerate(s):
            if char != '0':
                val = int(char) * (10 ** (length - 1 - i))
                ans.append(val)
        return ans

