class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [int(c) for c in str(n) if c != '0']
        if not digits:
            return 0
        
        # x を作る
        x = int(''.join(map(str, digits)))
        # 各桁の合計
        digit_sum = sum(digits)
        
        return x * digit_sum

