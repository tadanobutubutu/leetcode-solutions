class Solution:
    def canAliceWin(self, n: int) -> bool:
        needed = 10
        alice_turn = True
        while n >= needed:
            n -= needed
            needed -= 1
            alice_turn = not alice_turn
        return not alice_turn

