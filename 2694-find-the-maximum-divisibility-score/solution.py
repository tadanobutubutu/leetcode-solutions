class Solution:
    def maxDivScore(self, nums: list[int], divisors: list[int]) -> int:
        max_score = -1
        best_div = -1
        for d in divisors:
            score = 0
            for num in nums:
                if num % d == 0:
                    score += 1
            if score > max_score:
                max_score = score
                best_div = d
            elif score == max_score:
                if d < best_div:
                    best_div = d
        return best_div

