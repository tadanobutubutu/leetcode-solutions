class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = []
            for i in range(0, len(s), k):
                group = s[i:i+k]
                new_s.append(str(sum(int(c) for c in group)))
            s = "".join(new_s)
        return s

