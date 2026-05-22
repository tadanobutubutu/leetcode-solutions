from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [['' for _ in range(3)] for _ in range(3)]
        
        for i, (r, c) in enumerate(moves):
            grid[r][c] = 'A' if i % 2 == 0 else 'B'
            
        # 勝者の判定
        # 行の確認
        for r in range(3):
            if grid[r][0] == grid[r][1] == grid[r][2] != '':
                return grid[r][0]
                
        # 列の確認
        for c in range(3):
            if grid[0][c] == grid[1][c] == grid[2][c] != '':
                return grid[0][c]
                
        # 対角線の確認
        if grid[0][0] == grid[1][1] == grid[2][2] != '':
            return grid[0][0]
        if grid[0][2] == grid[1][1] == grid[2][0] != '':
            return grid[0][2]
            
        # 勝者がいない場合
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

