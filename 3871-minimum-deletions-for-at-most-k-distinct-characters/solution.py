from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counts = Counter(s)
        # 頻度を降順にソート
        freqs = sorted(counts.values(), reverse=True)
        # 上位 k 個の合計
        keep = sum(freqs[:k])
        # 削除数は全体の長さから残した数を引いたもの
        return len(s) - keep

