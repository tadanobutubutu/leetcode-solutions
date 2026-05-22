class Solution:
    def minOperations(self, s: str) -> int:
        ops_A = 0
        for i, char in enumerate(s):
            expected = str(i % 2)
            if char != expected:
                ops_A += 1
        return min(ops_A, len(s) - ops_A)

