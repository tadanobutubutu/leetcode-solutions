class Solution:
    def numDecodings(self, s: str) -> int:
        # 文字列が空、または最初の文字が '0' の場合はデコード不可
        if not s or s[0] == '0':
            return 0
            
        n = len(s)
        # 空間計算量 O(1) に最適化された動的計画法
        # two_back は dp[i-2], one_back は dp[i-1] に相当する
        two_back = 1  # dp[0]
        one_back = 1  # dp[1]
        
        for i in range(1, n):
            current = 0
            # 1. 1桁でデコードする場合（'0' でない場合のみ可能）
            if s[i] != '0':
                current += one_back
            
            # 2. 直前の文字と合わせて2桁でデコードする場合（"10" 〜 "26" の範囲）
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += two_back
                
            # 変数の更新
            two_back = one_back
            one_back = current
            
            # 途中でデコード方法が0になった場合は即座に終了して0を返す
            if one_back == 0:
                return 0
                
        return one_back

