from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        
        clockwise_dist = sum(distance[start:destination])
        total_dist = sum(distance)
        
        return min(clockwise_dist, total_dist - clockwise_dist)

