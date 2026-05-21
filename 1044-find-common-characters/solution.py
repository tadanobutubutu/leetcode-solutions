class Solution:
    def commonChars(self, words):
        from collections import Counter

        common = Counter(words[0])

        for w in words[1:]:
            common &= Counter(w)

        res = []
        for c, cnt in common.items():
            res.extend([c] * cnt)

        return res

