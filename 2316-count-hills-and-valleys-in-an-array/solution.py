from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        compressed = []
        for x in nums:
            if not compressed or compressed[-1] != x:
                compressed.append(x)
                
        count = 0
        for i in range(1, len(compressed) - 1):
            if (compressed[i] > compressed[i - 1] and compressed[i] > compressed[i + 1]) or \
               (compressed[i] < compressed[i - 1] and compressed[i] < compressed[i + 1]):
                count += 1
        return count

