class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                # 区間が途切れた
                if start == nums[i-1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i-1]}")
                start = nums[i]
        
        # 最後の区間を追加
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")
        
        return res

