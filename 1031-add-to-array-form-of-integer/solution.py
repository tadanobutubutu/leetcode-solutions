class Solution:
    def addToArrayForm(self, num, k):
        i = len(num) - 1
        carry = 0
        res = []

        while i >= 0 or k > 0 or carry:
            n = num[i] if i >= 0 else 0
            digit_k = k % 10
            k //= 10

            s = n + digit_k + carry
            res.append(s % 10)
            carry = s // 10

            i -= 1

        return res[::-1]

