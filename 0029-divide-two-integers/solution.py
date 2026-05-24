class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # コーナーケース：32ビット符号付き整数のオーバーフロー
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
            
        # 符号の決定
        negative = (dividend < 0) != (divisor < 0)
        
        # 絶対値に変換
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        # ビットシフトを用いた引き算の高速化
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            # temp * 2 が dividend 以下である限り、2倍にし続ける
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
                
            dividend -= temp
            quotient += multiple
            
        # 符号の適用
        if negative:
            quotient = -quotient
            
        # 範囲内にクランプ
        return min(max(INT_MIN, quotient), INT_MAX)

