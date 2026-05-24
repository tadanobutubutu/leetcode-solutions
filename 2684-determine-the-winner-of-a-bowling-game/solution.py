class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        def get_score(player):
            score = 0
            n = len(player)
            for i in range(n):
                double = False
                if i >= 1 and player[i - 1] == 10:
                    double = True
                if i >= 2 and player[i - 2] == 10:
                    double = True
                
                if double:
                    score += 2 * player[i]
                else:
                    score += player[i]
            return score
            
        score1 = get_score(player1)
        score2 = get_score(player2)
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0

