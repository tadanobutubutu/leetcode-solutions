class Solution:
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])
        ans = 0

        for col in range(m):
            for row in range(1, n):
                if strs[row][col] < strs[row - 1][col]:
                    ans += 1
                    break
        return ans

