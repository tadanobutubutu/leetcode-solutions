class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = number.replace("-", "").replace(" ", "")
        blocks = []
        i = 0
        n = len(digits)
        
        while n - i > 4:
            blocks.append(digits[i : i + 3])
            i += 3
            
        rem = n - i
        if rem == 4:
            blocks.append(digits[i : i + 2])
            blocks.append(digits[i + 2 : i + 4])
        elif rem == 3:
            blocks.append(digits[i : i + 3])
        elif rem == 2:
            blocks.append(digits[i : i + 2])
            
        return "-".join(blocks)

