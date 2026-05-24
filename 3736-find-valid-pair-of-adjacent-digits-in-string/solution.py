from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        counts = Counter(s)
        n = len(s)
        for i in range(n - 1):
            c1 = s[i]
            c2 = s[i + 1]
            if c1 != c2:
                if counts[c1] == int(c1) and counts[c2] == int(c2):
                    return c1 + c2
        return ""

