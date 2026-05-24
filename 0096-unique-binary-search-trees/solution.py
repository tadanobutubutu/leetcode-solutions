import math

class Solution:
    def numTrees(self, n: int) -> int:
        # ユニークな二分探索木の数は「カタラン数 (Catalan Number)」に等しい
        # カタラン数 C_n = (1 / (n + 1)) * comb(2n, n)
        # これを直接計算することで、動的計画法を使用せず O(n) の時間計算量かつ O(1) の空間計算量で計算できる
        return math.comb(2 * n, n) // (n + 1)

