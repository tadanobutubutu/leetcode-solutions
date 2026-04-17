class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n

        # 左→右
        prev = -10**9
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev

        # 右→左
        prev = 10**9
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans

