class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)
        sx = str(x)
        return (sx in s) and (not s.startswith(sx))

