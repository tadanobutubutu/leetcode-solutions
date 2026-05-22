from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration = releaseTimes[0]
        best_key = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            key = keysPressed[i]
            if duration > max_duration or (duration == max_duration and key > best_key):
                max_duration = duration
                best_key = key
        return best_key

