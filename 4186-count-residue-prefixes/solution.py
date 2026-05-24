class Solution:
    def residuePrefixes(self, s: str) -> int:
        seen = set()
        ans = 0
        for i, c in enumerate(s):
            seen.add(c)
            L = i + 1
            if len(seen) == L % 3:
                ans += 1
        return ans

