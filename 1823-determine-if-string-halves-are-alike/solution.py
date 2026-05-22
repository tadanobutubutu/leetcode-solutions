class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        half = len(s) // 2
        a = s[:half]
        b = s[half:]
        
        count_a = sum(1 for char in a if char in vowels)
        count_b = sum(1 for char in b if char in vowels)
        
        return count_a == count_b

