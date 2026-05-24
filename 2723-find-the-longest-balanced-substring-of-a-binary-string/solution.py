class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        i = 0
        while i < n:
            zeros = 0
            ones = 0
            while i < n and s[i] == '0':
                zeros += 1
                i += 1
            while i < n and s[i] == '1':
                ones += 1
                i += 1
            if zeros > 0 and ones > 0:
                ans = max(ans, 2 * min(zeros, ones))
        return ans

