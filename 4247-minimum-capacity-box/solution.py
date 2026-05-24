class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        min_cap = float('inf')
        ans_idx = -1
        
        for i, cap in enumerate(capacity):
            if cap >= itemSize:
                if cap < min_cap:
                    min_cap = cap
                    ans_idx = i
                    
        return ans_idx

