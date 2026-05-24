class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            # i番目の文字を削除した新しい文字列を作成
            new_word = word[:i] + word[i+1:]
            
            # 各文字の出現頻度をカウント
            counts = {}
            for char in new_word:
                counts[char] = counts.get(char, 0) + 1
            
            # 出現頻度のユニークな値の数が1つであれば、すべての文字の頻度が等しい
            if len(set(counts.values())) == 1:
                return True
        return False

