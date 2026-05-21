class Solution:
    def isAlienSorted(self, words, order):
        rank = {c: i for i, c in enumerate(order)}

        def in_order(w1, w2):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    return rank[c1] < rank[c2]
            return len(w1) <= len(w2)

        for i in range(len(words) - 1):
            if not in_order(words[i], words[i + 1]):
                return False
        return True

