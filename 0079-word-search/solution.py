from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        
        # 1. 枝刈り：ボード上の文字数が足りない場合は即時False
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
                
        # 2. 枝刈り：開始文字の出現頻度が終了文字の出現頻度より大きい場合、
        # 単語を反転させることで、探索の開始分岐を減らし高速化する
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
            
        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != word[i]:
                return False
                
            # 訪問済みをマークするため一時的に文字を書き換える
            temp = board[r][c]
            board[r][c] = "#"
            
            # 隣接する4方向を探索
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))
                     
            # バックトラック：元の文字に戻す
            board[r][c] = temp
            return found
            
        for r in range(R):
            for c in range(C):
                # 最初の文字が一致するセルから探索を開始
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
                        
        return False

