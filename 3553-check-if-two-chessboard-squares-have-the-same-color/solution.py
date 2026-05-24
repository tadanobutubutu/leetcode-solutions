class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        color1 = (ord(coordinate1[0]) + ord(coordinate1[1])) % 2
        color2 = (ord(coordinate2[0]) + ord(coordinate2[1])) % 2
        return color1 == color2

