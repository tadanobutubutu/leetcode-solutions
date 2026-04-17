class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        js = set(jewels)
        return sum(s in js for s in stones)

