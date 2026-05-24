class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s, start=1):
            rev_alphabet_idx = 26 - (ord(char) - ord('a'))
            total += rev_alphabet_idx * i
        return total

