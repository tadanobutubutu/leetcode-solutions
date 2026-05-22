import math

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(k):
            if k < 2:
                return False
            for i in range(2, int(math.isqrt(k)) + 1):
                if k % i == 0:
                    return False
            return True

        num_primes = sum(1 for i in range(1, n + 1) if is_prime(i))
        num_non_primes = n - num_primes
        
        MOD = 10**9 + 7
        return (math.factorial(num_primes) * math.factorial(num_non_primes)) % MOD

