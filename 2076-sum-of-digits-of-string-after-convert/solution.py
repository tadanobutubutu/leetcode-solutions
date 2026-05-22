class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = "".join(str(ord(c) - ord('a') + 1) for c in s)
        for _ in range(k):
            val = sum(int(digit) for digit in num_str)
            num_str = str(val)
        return int(num_str)

