from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        return "".join(w[0] for w in words) == s

