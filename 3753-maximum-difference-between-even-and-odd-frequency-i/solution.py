from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        odd_freqs = []
        even_freqs = []
        for char, freq in counts.items():
            if freq % 2 == 1:
                odd_freqs.append(freq)
            else:
                even_freqs.append(freq)
        return max(odd_freqs) - min(even_freqs)

