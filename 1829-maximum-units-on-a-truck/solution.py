from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        for num_boxes, units in boxTypes:
            if truckSize <= 0:
                break
            take = min(num_boxes, truckSize)
            total_units += take * units
            truckSize -= take
            
        return total_units

