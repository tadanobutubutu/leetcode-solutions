from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0
        for i in range(n):
            left = colors[i - 1] # Pythonは負のインデックスに対応しているので、i=0 の時は -1、すなわち最後の要素になります
            mid = colors[i]
            right = colors[(i + 1) % n]
            if mid != left and mid != right:
                count += 1
        return count

