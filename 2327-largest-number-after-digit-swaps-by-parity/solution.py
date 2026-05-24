class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)
        evens = sorted([c for c in s if int(c) % 2 == 0], reverse=True)
        odds = sorted([c for c in s if int(c) % 2 != 0], reverse=True)
        
        even_idx = 0
        odd_idx = 0
        ans = []
        for c in s:
            val = int(c)
            if val % 2 == 0:
                ans.append(evens[even_idx])
                even_idx += 1
            else:
                ans.append(odds[odd_idx])
                odd_idx += 1
        return int("".join(ans))

