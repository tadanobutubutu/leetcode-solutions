class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occurrence = {}
        max_len = -1
        for i, char in enumerate(s):
            if char in first_occurrence:
                length = i - first_occurrence[char] - 1
                if length > max_len:
                    max_len = length
            else:
                first_occurrence[char] = i
        return max_len

