class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(int(d) for d in num[0::2]) == sum(int(d) for d in num[1::2])

