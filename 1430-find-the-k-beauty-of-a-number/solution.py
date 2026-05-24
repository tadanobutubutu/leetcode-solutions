class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        ans = 0
        for i in range(len(s) - k + 1):
            sub = s[i:i+k]
            val = int(sub)
            if val != 0 and num % val == 0:
                ans += 1
        return ans

