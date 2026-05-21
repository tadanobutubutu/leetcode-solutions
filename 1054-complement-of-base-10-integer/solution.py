class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1  # 特例（説明にも 0 はコーナーケースとある）

        mask = (1 << n.bit_length()) - 1
        return n ^ mask

