class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = 0
        count0 = 0
        count1 = 0
        ans = 0
        for right in range(len(s)):
            if s[right] == '0':
                count0 += 1
            else:
                count1 += 1
            
            # 条件（0の個数 <= k または 1の個数 <= k）を満たさない間、ウィンドウを縮小
            while count0 > k and count1 > k:
                if s[left] == '0':
                    count0 -= 1
                else:
                    count1 -= 1
                left += 1
            
            ans += (right - left + 1)
        return ans

