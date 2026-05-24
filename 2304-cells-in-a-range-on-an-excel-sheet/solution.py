from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1, row1, col2, row2 = s[0], int(s[1]), s[3], int(s[4])
        res = []
        for c in range(ord(col1), ord(col2) + 1):
            for r in range(row1, row2 + 1):
                res.append(chr(c) + str(r))
        return res

