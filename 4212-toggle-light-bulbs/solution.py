class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on_bulbs = set()
        for b in bulbs:
            if b in on_bulbs:
                on_bulbs.remove(b)
            else:
                on_bulbs.add(b)
        return sorted(list(on_bulbs))

