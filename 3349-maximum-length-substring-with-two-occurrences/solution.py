from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        counts = Counter()
        for right in range(len(s)):
            counts[s[right]] += 1
            while counts[s[right]] > 2:
                counts[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

