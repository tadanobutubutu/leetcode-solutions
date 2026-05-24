class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
            
        curr = "1"
        for _ in range(n - 1):
            next_str = []
            i = 0
            n_len = len(curr)
            
            while i < n_len:
                count = 1
                # 同じ文字が連続している間、カウントを増やす
                while i + 1 < n_len and curr[i] == curr[i + 1]:
                    count += 1
                    i += 1
                
                # count と文字自体を追加
                next_str.append(str(count))
                next_str.append(curr[i])
                i += 1
                
            curr = "".join(next_str)
            
        return curr

