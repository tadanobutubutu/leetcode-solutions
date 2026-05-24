from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for word in words:
            w = sum(weights[ord(c) - ord('a')] for c in word)
            mapped = chr(ord('z') - (w % 26))
            ans.append(mapped)
        return "".join(ans)

