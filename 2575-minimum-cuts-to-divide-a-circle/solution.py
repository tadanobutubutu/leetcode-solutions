class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        # 偶数の場合は直径で切れるため n // 2 回、奇数の場合は n 回
        return n // 2 if n % 2 == 0 else n

