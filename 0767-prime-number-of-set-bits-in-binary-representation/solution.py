class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # 問題で出る set bits の最大値は 20 以下なので、
        # 20 以下の素数をあらかじめセットにしておく
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        ans = 0
        for x in range(left, right + 1):
            # bin(x).count("1") で set bits の数を取る
            if bin(x).count("1") in primes:
                ans += 1

        return ans

