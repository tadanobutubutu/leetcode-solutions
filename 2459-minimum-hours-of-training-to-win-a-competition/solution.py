from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        sum_energy = sum(energy)
        extra_energy = max(0, sum_energy + 1 - initialEnergy)
        
        extra_experience = 0
        curr_exp = initialExperience
        for exp in experience:
            if curr_exp <= exp:
                diff = exp - curr_exp + 1
                extra_experience += diff
                curr_exp += diff
            curr_exp += exp
            
        return extra_energy + extra_experience

