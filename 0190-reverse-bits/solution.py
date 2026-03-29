class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # nの最下位ビットを取り出す
            bit = n & 1
            # 結果を左シフトしてビットを追加
            result = (result << 1) | bit
            # nを右シフトして次のビットへ
            n >>= 1
        return result

