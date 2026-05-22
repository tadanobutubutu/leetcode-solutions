class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        result = [""] * len(words)
        for word in words:
            actual_word = word[:-1]
            pos = int(word[-1]) - 1
            result[pos] = actual_word
        return " ".join(result)

