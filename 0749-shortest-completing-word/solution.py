from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # licensePlate の文字カウント（英字のみ、小文字化）
        need = Counter(ch.lower() for ch in licensePlate if ch.isalpha())

        ans = None

        for w in words:
            c = Counter(w)
            ok = True
            for ch, cnt in need.items():
                if c[ch] < cnt:
                    ok = False
                    break

            if ok:
                if ans is None or len(w) < len(ans):
                    ans = w

        return ans

