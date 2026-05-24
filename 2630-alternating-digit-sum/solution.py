class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        ans = 0
        sign = 1
        for char in s:
            ans += sign * int(char)
            sign = -sign
        return ans

