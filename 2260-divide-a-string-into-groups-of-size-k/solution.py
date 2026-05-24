from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0, len(s), k):
            sub = s[i:i+k]
            if len(sub) < k:
                sub += fill * (k - len(sub))
            ans.append(sub)
        return ans

