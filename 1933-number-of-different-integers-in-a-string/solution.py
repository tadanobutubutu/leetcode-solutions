class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        replaced = "".join(char if char.isdigit() else ' ' for char in word)
        unique_ints = {int(token) for token in replaced.split()}
        return len(unique_ints)

