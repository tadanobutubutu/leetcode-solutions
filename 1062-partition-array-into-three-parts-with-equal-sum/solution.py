class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        count = 0
        curr = 0

        for x in arr:
            curr += x
            if curr == target:
                count += 1
                curr = 0
            if count == 3:
                return True

        return False

