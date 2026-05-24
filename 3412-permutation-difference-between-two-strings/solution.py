class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_indices = {char: idx for idx, char in enumerate(s)}
        t_indices = {char: idx for idx, char in enumerate(t)}
        
        diff = 0
        for char in s_indices:
            diff += abs(s_indices[char] - t_indices[char])
            
        return diff

