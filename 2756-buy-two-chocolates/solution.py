class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        min1 = float('inf')
        min2 = float('inf')
        for p in prices:
            if p < min1:
                min2 = min1
                min1 = p
            elif p < min2:
                min2 = p
        
        cost = min1 + min2
        return money - cost if cost <= money else money

