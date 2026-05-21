class Solution:
    def diStringMatch(self, s: str):
        low, high = 0, len(s)
        ans = []

        for c in s:
            if c == 'I':
                ans.append(low)
                low += 1
            else:  # 'D'
                ans.append(high)
                high -= 1

        ans.append(low)  # 最後は low == high
        return ans

