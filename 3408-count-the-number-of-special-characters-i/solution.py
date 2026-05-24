class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_set = set(word)
        count = 0
        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)
            if lower in char_set and upper in char_set:
                count += 1
        return count

