class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # 長さが違うなら絶対に無理
        if len(s) != len(goal):
            return False

        # 同じ文字列の場合 → 重複文字があれば swap しても同じになる
        if s == goal:
            return len(set(s)) < len(s)

        # 違う文字の位置を集める
        diff = []
        for a, b in zip(s, goal):
            if a != b:
                diff.append((a, b))
                if len(diff) > 2:
                    return False

        # ちょうど2箇所違っていて、swap で一致するならOK
        return len(diff) == 2 and diff[0] == diff[1][::-1]

