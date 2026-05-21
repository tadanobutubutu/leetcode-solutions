from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck).values()
        g = 0
        for c in counts:
            g = math.gcd(g, c)
        return g >= 2
