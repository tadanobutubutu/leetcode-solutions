class Solution:
    def splitNum(self, num: int) -> int:
        s = sorted(str(num))
        num1 = "".join(s[::2])
        num2 = "".join(s[1::2])
        return int(num1) + int(num2)

