class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)

        for i in range(0, n, 2 * k):
            # i から i+k の範囲を反転（範囲外は自動で調整される）
            s[i:i+k] = reversed(s[i:i+k])

        return "".join(s)

