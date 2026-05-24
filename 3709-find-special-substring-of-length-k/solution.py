class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        for i in range(n - k + 1):
            sub = s[i : i + k]
            # 1種類の文字のみで構成されているか
            if len(set(sub)) == 1:
                char = sub[0]
                # 直前の文字のチェック
                if i > 0 and s[i - 1] == char:
                    continue
                # 直後の文字のチェック
                if i + k < n and s[i + k] == char:
                    continue
                # すべての条件を満たす
                return True
        return False

