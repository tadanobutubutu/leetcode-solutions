from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        
        while i < n1 and j < n2:
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            
            if id1 == id2:
                ans.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                ans.append([id1, val1])
                i += 1
            else:
                ans.append([id2, val2])
                j += 1
                
        while i < n1:
            ans.append(nums1[i])
            i += 1
            
        while j < n2:
            ans.append(nums2[j])
            j += 1
            
        return ans

