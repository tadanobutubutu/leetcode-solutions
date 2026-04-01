class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        # 32bit two's complement に合わせる
        num &= 0xffffffff

        hex_chars = "0123456789abcdef"
        res = []

        while num > 0:
            res.append(hex_chars[num & 0xf])  # 下位4bitを取り出す
            num >>= 4                         # 4bit 右シフト

        return "".join(reversed(res))

