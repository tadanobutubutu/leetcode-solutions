from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        # Count frequencies of all characters in the string
        counts = Counter(s)
        # Get sorted list of unique characters
        chars = sorted(counts.keys())
        res = []
        n = len(s)
        
        while len(res) < n:
            # 1. Increasing phase (a to z)
            for char in chars:
                if counts[char] > 0:
                    res.append(char)
                    counts[char] -= 1
            # 2. Decreasing phase (z to a)
            for char in reversed(chars):
                if counts[char] > 0:
                    res.append(char)
                    counts[char] -= 1
                    
        return "".join(res)

