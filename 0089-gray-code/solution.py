from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 数学的なグレイコードの定義: G(i) = i ^ (i >> 1)
        # 0 から 2^n - 1 までの各整数に対してこの数式を適用することで、
        # 隣接要素および始端・終端の間で1ビットのみ変化するシーケンスをO(2^n)で生成できる
        return [i ^ (i >> 1) for i in range(1 << n)]

