from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pop = [0] * 102
        for birth, death in logs:
            pop[birth - 1950] += 1
            pop[death - 1950] -= 1
        
        max_pop = 0
        max_year = 1950
        current_pop = 0
        for i in range(101):
            current_pop += pop[i]
            if current_pop > max_pop:
                max_pop = current_pop
                max_year = 1950 + i
        return max_year

