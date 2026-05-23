class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        n = len(word)
        for i in range(n):
            current_vowels = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                current_vowels.add(word[j])
                if len(current_vowels) == 5:
                    count += 1
        return count

