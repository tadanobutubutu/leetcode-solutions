class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        max1 = max(nums)
        idx = nums.index(max1)

        # max1 を除いた中での 2 番目に大きい値
        max2 = max(n for n in nums if n != max1)

        return idx if max1 >= 2 * max2 else -1

