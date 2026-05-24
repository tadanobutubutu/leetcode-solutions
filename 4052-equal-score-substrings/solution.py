class Solution:
    def scoreBalance(self, s: str) -> bool:
        scores = [ord(c) - ord('a') + 1 for c in s]
        total_score = sum(scores)
        if total_score % 2 != 0:
            return False
        
        target = total_score // 2
        curr = 0
        for i in range(len(scores) - 1):
            curr += scores[i]
            if curr == target:
                return True
        return False

