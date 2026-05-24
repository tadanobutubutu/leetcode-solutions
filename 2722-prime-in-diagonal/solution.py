class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2 or n == 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
            
        n = len(nums)
        max_prime = 0
        for i in range(n):
            val1 = nums[i][i]
            if val1 > max_prime and is_prime(val1):
                max_prime = val1
            val2 = nums[i][n - i - 1]
            if val2 > max_prime and is_prime(val2):
                max_prime = val2
        return max_prime

