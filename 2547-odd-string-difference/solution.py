from typing import List

class Solution:
    def oddString(self, words: List[str]) -> str:
        diff_map = {}
        for word in words:
            # 隣接する文字のインデックスの差分を計算
            diff = []
            for i in range(len(word) - 1):
                diff.append(ord(word[i+1]) - ord(word[i]))
            diff_tuple = tuple(diff)
            
            if diff_tuple not in diff_map:
                diff_map[diff_tuple] = []
            diff_map[diff_tuple].append(word)
            
        # 出現回数が1回だけの差分パターンに対応する単語を返す
        for word_list in diff_map.values():
            if len(word_list) == 1:
                return word_list[0]

