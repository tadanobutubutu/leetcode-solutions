class Solution:
    def circularGameLosers(self, n: int, k: int) -> list[int]:
        visited = {0}
        curr = 0
        i = 1
        while True:
            curr = (curr + i * k) % n
            if curr in visited:
                break
            visited.add(curr)
            i += 1
        
        return [j + 1 for j in range(n) if j not in visited]

