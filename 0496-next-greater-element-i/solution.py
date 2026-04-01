class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge = {}  # next greater element map

        for num in nums2:
            while stack and stack[-1] < num:
                nge[stack.pop()] = num
            stack.append(num)

        # 残ったものは次に大きい要素がない
        for num in stack:
            nge[num] = -1

        return [nge[x] for x in nums1]

