class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e, o = 0, 1
        n = len(nums)
        while e < n and o < n:
            if nums[e] % 2 == 0:
                e += 2
            elif nums[o] % 2 != 0:
                o += 2
            else:
                nums[e], nums[o] = nums[o], nums[e]
                e += 2
                o += 2
        return nums
