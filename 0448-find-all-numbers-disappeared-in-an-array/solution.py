class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        res = []
        for i, v in enumerate(nums):
            if v > 0:
                res.append(i + 1)

        return res

