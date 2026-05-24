class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        common = s1.intersection(s2)
        if common:
            return min(common)
        
        m1 = min(nums1)
        m2 = min(nums2)
        return min(m1 * 10 + m2, m2 * 10 + m1)

