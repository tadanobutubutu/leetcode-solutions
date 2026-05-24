class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        # 文字数の合計が一致しない場合はインターリーブ不可
        if n1 + n2 != n3:
            return False
            
        # s2の長さを基準にするため、s1の方が短い場合は入れ替えて
        # 追加メモリ空間を O(min(len(s1), len(s2))) に最適化する
        if n1 < n2:
            s1, s2 = s2, s1
            n1, n2 = n2, n1
            
        # dp[j] は s1 の最初の i 文字と s2 の最初の j 文字で
        # s3 の最初の i + j 文字を形成できるかを表す
        dp = [False] * (n2 + 1)
        dp[0] = True
        
        # 1行目（s1が空の状態）の初期化
        for j in range(1, n2 + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        for i in range(1, n1 + 1):
            # 各行の開始時点（s2が空の状態）の更新
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            
            for j in range(1, n2 + 1):
                # s1の文字を使う場合 (dp[j] は直前の行のj列目、すなわち dp[i-1][j])
                # s2の文字を使う場合 (dp[j-1] は現在の行のj-1列目、すなわち dp[i][j-1])
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or \
                        (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                        
        return dp[n2]

