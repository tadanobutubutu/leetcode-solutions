from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        # 2つの時間区間 [S1, E1] と [S2, E2] が交差する条件は、max(S1, S2) <= min(E1, E2)
        return max(event1[0], event2[0]) <= min(event1[1], event2[1])

