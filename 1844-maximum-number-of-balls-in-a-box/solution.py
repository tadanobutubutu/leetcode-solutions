class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counts = [0] * 46
        for num in range(lowLimit, highLimit + 1):
            s = 0
            temp = num
            while temp > 0:
                s += temp % 10
                temp //= 10
            counts[s] += 1
        return max(counts)

