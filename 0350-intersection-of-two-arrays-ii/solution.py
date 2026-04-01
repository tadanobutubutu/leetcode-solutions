from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        res = []
        for x in nums2:
            if count[x] > 0:
                res.append(x)
                count[x] -= 1
        return res

