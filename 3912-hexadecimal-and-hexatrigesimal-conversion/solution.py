class Solution:
    def concatHex36(self, n: int) -> str:
        # n^2 の16進数表現（大文字）
        hex_rep = hex(n * n)[2:].upper()
        
        # n^3 の36進数表現（大文字）
        val36 = n * n * n
        if val36 == 0:
            base36_rep = "0"
        else:
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            res = []
            x = val36
            while x > 0:
                res.append(digits[x % 36])
                x //= 36
            base36_rep = "".join(reversed(res))
            
        return hex_rep + base36_rep

