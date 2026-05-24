from typing import List
from collections import defaultdict

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        player_picks = [defaultdict(int) for _ in range(n)]
        for x, y in pick:
            player_picks[x][y] += 1
            
        winners = 0
        for i in range(n):
            # プレイヤーiが同じ色のボールを少なくとも i + 1 個取得したかを判定
            if any(count >= i + 1 for count in player_picks[i].values()):
                winners += 1
        return winners

