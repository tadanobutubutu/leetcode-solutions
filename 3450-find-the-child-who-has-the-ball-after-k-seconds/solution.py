class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        round_trip = 2 * (n - 1)
        rem = k % round_trip
        if rem <= n - 1:
            return rem
        else:
            return round_trip - rem

