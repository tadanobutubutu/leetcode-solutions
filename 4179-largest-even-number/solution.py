class Solution:
    def largestEven(self, s: str) -> str:
        idx = s.rfind('2')
        if idx == -1:
            return ""
        return s[:idx+1]

