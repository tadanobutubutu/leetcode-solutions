class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if not nums:
            return []
        res = set(nums[0])
        for x in nums[1:]:
            res &= set(x)
        return sorted(list(res))

