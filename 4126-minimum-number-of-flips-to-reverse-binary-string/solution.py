class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        r = s[::-1]
        ans = 0
        for c1, c2 in zip(s, r):
            if c1 != c2:
                ans += 1
        return ans

