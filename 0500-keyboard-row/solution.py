class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        res = []
        for w in words:
            lower = set(w.lower())
            if lower <= row1 or lower <= row2 or lower <= row3:
                res.append(w)
        return res

