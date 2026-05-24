class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n = min(len(s1), len(s2), len(s3))
        L = 0
        while L < n and s1[L] == s2[L] == s3[L]:
            L += 1
            
        if L == 0:
            return -1
            
        return len(s1) + len(s2) + len(s3) - 3 * L

