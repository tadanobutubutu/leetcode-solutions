from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_mag = Counter(magazine)
        for ch in ransomNote:
            if count_mag[ch] == 0:
                return False
            count_mag[ch] -= 1
        return True

