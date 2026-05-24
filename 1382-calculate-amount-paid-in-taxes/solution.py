from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income == 0:
            return 0.0
            
        total_tax = 0.0
        prev_upper = 0
        
        for upper, percent in brackets:
            if income > prev_upper:
                taxable = min(income, upper) - prev_upper
                total_tax += taxable * (percent / 100.0)
                prev_upper = upper
            else:
                break
                
        return total_tax

