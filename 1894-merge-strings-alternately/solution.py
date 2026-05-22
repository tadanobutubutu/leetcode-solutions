class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for c1, c2 in zip(word1, word2):
            merged.append(c1)
            merged.append(c2)
        
        min_len = min(len(word1), len(word2))
        merged.append(word1[min_len:])
        merged.append(word2[min_len:])
        
        return "".join(merged)

