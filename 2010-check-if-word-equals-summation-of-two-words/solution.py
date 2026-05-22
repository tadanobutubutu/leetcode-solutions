class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def to_int(word: str) -> int:
            return int("".join(str(ord(c) - 97) for c in word))
        
        return to_int(firstWord) + to_int(secondWord) == to_int(targetWord)

