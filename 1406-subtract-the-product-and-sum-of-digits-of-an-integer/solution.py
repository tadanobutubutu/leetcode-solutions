class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        prod_val = 1
        sum_val = 0
        for d in digits:
            prod_val *= d
            sum_val += d
        return prod_val - sum_val

