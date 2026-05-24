import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        
        # 英数字とアンダースコアのみ、空でない
        pattern = re.compile(r'^[a-zA-Z0-9_]+$')
        
        valid_coupons = []
        for i in range(len(code)):
            if isActive[i] and businessLine[i] in order and pattern.match(code[i]):
                valid_coupons.append((code[i], businessLine[i]))
                
        # businessLine の優先順、および code の辞書順でソート
        valid_coupons.sort(key=lambda x: (order[x[1]], x[0]))
        
        return [x[0] for x in valid_coupons]

