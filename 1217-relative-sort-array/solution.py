from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = {val: idx for idx, val in enumerate(arr2)}
        
        def sort_key(x):
            if x in pos:
                return (0, pos[x])
            else:
                return (1, x)
                
        return sorted(arr1, key=sort_key)

