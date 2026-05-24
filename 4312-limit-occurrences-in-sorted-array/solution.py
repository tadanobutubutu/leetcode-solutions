class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans = []
        count = 0
        last = None
        for x in nums:
            if x != last:
                last = x
                count = 1
                ans.append(x)
            else:
                if count < k:
                    count += 1
                    ans.append(x)
        return ans

