class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n + 1)

        for x in nums:
            count[x] += 1

        dup = miss = -1
        for i in range(1, n + 1):
            if count[i] == 2:
                dup = i
            elif count[i] == 0:
                miss = i

        return [dup, miss]

