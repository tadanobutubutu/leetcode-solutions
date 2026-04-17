class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        n = len(s)
        i = 0

        while i < n:
            j = i
            # 同じ文字が続く区間を伸ばす
            while j < n and s[j] == s[i]:
                j += 1

            # 長さが 3 以上なら large group
            if j - i >= 3:
                res.append([i, j - 1])

            i = j

        return res

