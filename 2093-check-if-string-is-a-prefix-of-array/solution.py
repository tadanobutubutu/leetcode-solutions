from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        concat = ""
        for w in words:
            concat += w
            if concat == s:
                return True
            if len(concat) > len(s):
                return False
        return False

