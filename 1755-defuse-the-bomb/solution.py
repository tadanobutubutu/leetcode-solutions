from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        extended = code + code
        res = []
        if k > 0:
            for i in range(n):
                res.append(sum(extended[i + 1 : i + 1 + k]))
        else:
            for i in range(n):
                res.append(sum(extended[i + n + k : i + n]))
                
        return res

