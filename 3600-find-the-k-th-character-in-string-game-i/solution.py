class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            next_word = "".join(
                chr((ord(char) - 97 + 1) % 26 + 97) for char in word
            )
            word += next_word
        return word[k-1]

