class Solution:
    def greatestLetter(self, s: str) -> str:
        s_set = set(s)
        for i in range(25, -1, -1):
            upper_char = chr(ord('A') + i)
            lower_char = chr(ord('a') + i)
            if upper_char in s_set and lower_char in s_set:
                return upper_char
        return ""

