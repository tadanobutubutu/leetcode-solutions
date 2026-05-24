class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        period = n - 1
        full_rounds = time // period
        extra_time = time % period
        
        if full_rounds % 2 == 0:
            return 1 + extra_time
        else:
            return n - extra_time

