from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 1. 右側から隣り合う要素で昇順になっている最初の位置（i）を探す
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:
            # 2. i より右側で、nums[i] より大きい最初の要素（j）を右側から探す
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 3. スワップする
            nums[i], nums[j] = nums[j], nums[i]
            
        # 4. i + 1 から末尾までの部分配列を反転（reverse）させる
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

