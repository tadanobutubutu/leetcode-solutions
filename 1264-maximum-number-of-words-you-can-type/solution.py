from typing import List

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        words = text.split()
        count = 0
        for word in words:
            if not (set(word) & broken_set):
                count += 1
        return count

