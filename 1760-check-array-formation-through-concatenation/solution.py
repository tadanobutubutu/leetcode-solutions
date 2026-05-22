from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mapping = {p[0]: p for p in pieces}
        i = 0
        n = len(arr)
        while i < n:
            val = arr[i]
            if val not in mapping:
                return False
            p = mapping[val]
            if arr[i : i + len(p)] != p:
                return False
            i += len(p)
        return True

