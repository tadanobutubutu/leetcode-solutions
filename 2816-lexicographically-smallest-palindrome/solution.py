class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        chars = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if chars[i] != chars[j]:
                smaller = min(chars[i], chars[j])
                chars[i] = smaller
                chars[j] = smaller
            i += 1
            j -= 1
        return "".join(chars)

