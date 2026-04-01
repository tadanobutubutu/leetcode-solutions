class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = None

        for n in nums:
            if n == max1 or n == max2 or n == max3:
                continue

            if max1 is None or n > max1:
                max1, max2, max3 = n, max1, max2
            elif max2 is None or n > max2:
                max2, max3 = n, max2
            elif max3 is None or n > max3:
                max3 = n

        return max3 if max3 is not None else max1

