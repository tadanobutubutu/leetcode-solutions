class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for x in range(low, high + 1):
            s = str(x)
            n = len(s)
            if n % 2 == 0:
                mid = n // 2
                left = sum(int(c) for c in s[:mid])
                right = sum(int(c) for c in s[mid:])
                if left == right:
                    count += 1
        return count

