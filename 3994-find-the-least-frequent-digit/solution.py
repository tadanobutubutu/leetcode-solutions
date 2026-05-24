from collections import Counter

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s = str(n)
        counts = Counter(s)
        best_digit = min(counts.keys(), key=lambda d: (counts[d], int(d)))
        return int(best_digit)

