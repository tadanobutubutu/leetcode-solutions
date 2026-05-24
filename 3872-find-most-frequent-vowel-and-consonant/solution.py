from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        counts = Counter(s)
        
        max_vowel = 0
        max_consonant = 0
        
        for char, count in counts.items():
            if char in vowels:
                if count > max_vowel:
                    max_vowel = count
            else:
                if count > max_consonant:
                    max_consonant = count
                    
        return max_vowel + max_consonant

