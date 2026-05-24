from typing import List

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        best_button = events[0][0]
        max_time = events[0][1]
        
        for i in range(1, len(events)):
            duration = events[i][1] - events[i-1][1]
            btn = events[i][0]
            if duration > max_time:
                max_time = duration
                best_button = btn
            elif duration == max_time:
                if btn < best_button:
                    best_button = btn
                    
        return best_button

