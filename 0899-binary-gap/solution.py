class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        ans = 0
        i = 0

        while n > 0:
            if n & 1:
                if last != -1:
                    ans = max(ans, i - last)
                last = i
            i += 1
            n >>= 1

        return ans

