class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(c) for c in s]
        while len(digits) > 2:
            new_digits = []
            for i in range(len(digits) - 1):
                new_val = (digits[i] + digits[i + 1]) % 10
                new_digits.append(new_val)
            digits = new_digits
        return digits[0] == digits[1]

