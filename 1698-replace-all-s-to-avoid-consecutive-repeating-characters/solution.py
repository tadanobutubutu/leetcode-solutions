class Solution:
    def modifyString(self, s: str) -> str:
        res = list(s)
        n = len(res)
        for i in range(n):
            if res[i] == '?':
                for char in ('a', 'b', 'c'):
                    prev_char = res[i - 1] if i > 0 else ''
                    next_char = res[i + 1] if i < n - 1 else ''
                    if char != prev_char and char != next_char:
                        res[i] = char
                        break
        return "".join(res)

