from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_seen = -1
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = max_seen
            if curr > max_seen:
                max_seen = curr
        return arr

