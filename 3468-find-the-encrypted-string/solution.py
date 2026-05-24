class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        shift = k % n
        return s[shift:] + s[:shift]

