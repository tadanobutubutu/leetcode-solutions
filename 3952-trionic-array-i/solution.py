from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False
            
        for p in range(1, n - 2):
            # seg1 が [0...p] で増加しているか先にチェック（枝刈り）
            seg1_ok = True
            for i in range(0, p):
                if nums[i] >= nums[i+1]:
                    seg1_ok = False
                    break
            if not seg1_ok:
                continue
                
            for q in range(p + 1, n - 1):
                # seg2 が [p...q] で減少しているかチェック
                seg2_ok = True
                for i in range(p, q):
                    if nums[i] <= nums[i+1]:
                        seg2_ok = False
                        break
                if not seg2_ok:
                    continue
                    
                # seg3 が [q...n-1] で増加しているかチェック
                seg3_ok = True
                for i in range(q, n - 1):
                    if nums[i] >= nums[i+1]:
                        seg3_ok = False
                        break
                if not seg3_ok:
                    continue
                    
                return True
                
        return False

