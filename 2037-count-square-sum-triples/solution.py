import math

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                val = a * a + b * b
                c = math.isqrt(val)
                if c <= n and c * c == val:
                    ans += 1
        return ans

