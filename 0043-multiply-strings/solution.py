class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        # 後ろから走査
        for i in range(m - 1, -1, -1):
            n1 = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                n2 = ord(num2[j]) - ord('0')
                mul = n1 * n2
                
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]
                
                res[p2] = total % 10
                res[p1] += total // 10
                
        # 先頭のゼロを取り除く
        result = []
        for x in res:
            if not (len(result) == 0 and x == 0):
                result.append(str(x))
                
        return "".join(result) if result else "0"

