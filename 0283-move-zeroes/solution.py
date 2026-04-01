class Solution:
    def moveZeroes(self, nums):
        insert_pos = 0  # 非ゼロを書き込む位置

        # 1. 非ゼロを前に詰める
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # 2. 残りを 0 で埋める
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

