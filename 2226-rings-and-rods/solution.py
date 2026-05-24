class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {str(i): set() for i in range(10)}
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = rings[i+1]
            rods[rod].add(color)
        
        ans = 0
        for colors in rods.values():
            if len(colors) == 3:
                ans += 1
        return ans

