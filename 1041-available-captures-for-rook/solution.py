class Solution:
    def numRookCaptures(self, board):
        # 1. ルークの位置を探す
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    rook_r, rook_c = r, c

        ans = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]  # 下・上・右・左

        # 2. 4方向に進む
        for dr, dc in dirs:
            nr, nc = rook_r + dr, rook_c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == 'B':  # bishop がブロック 
                    break
                if board[nr][nc] == 'p':  # pawn を捕獲できる 
                    ans += 1
                    break
                nr += dr
                nc += dc

        return ans

