class Solution:
    def checkRecord(self, s: str) -> bool:
        # 条件1: 'A' が 2 回以上ならアウト
        if s.count('A') >= 2:
            return False

        # 条件2: 'LLL' が含まれていたらアウト
        if "LLL" in s:
            return False

        return True

