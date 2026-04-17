class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        res = []

        for i, w in enumerate(words, 1):
            if w[0] in vowels:
                new_w = w + "ma"
            else:
                new_w = w[1:] + w[0] + "ma"
            new_w += "a" * i
            res.append(new_w)

        return " ".join(res)

