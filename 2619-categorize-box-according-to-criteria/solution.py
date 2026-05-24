class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky = (
            length >= 10000 or
            width >= 10000 or
            height >= 10000 or
            (length * width * height) >= 1000000000
        )
        is_heavy = mass >= 100
        
        if is_bulky and is_heavy:
            return "Both"
        if not is_bulky and not is_heavy:
            return "Neither"
        if is_bulky:
            return "Bulky"
        return "Heavy"

