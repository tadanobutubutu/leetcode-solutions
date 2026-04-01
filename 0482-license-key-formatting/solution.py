class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # 1. ダッシュを除去して大文字化
        s = s.replace("-", "").upper()

        # 2. 右から k 文字ずつグループ化
        res = []
        while len(s) > k:
            res.append(s[-k:])
            s = s[:-k]

        # 3. 最後に残った先頭グループを追加
        res.append(s)

        # 4. 逆順にして結合
        return "-".join(res[::-1])

