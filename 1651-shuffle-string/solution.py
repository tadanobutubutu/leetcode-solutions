from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [None] * len(s)
        for char, idx in zip(s, indices):
            ans[idx] = char
        return "".join(ans)

