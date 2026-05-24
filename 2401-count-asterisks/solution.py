class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        inside = False
        for char in s:
            if char == '|':
                inside = not inside
            elif char == '*':
                if not inside:
                    ans += 1
        return ans

