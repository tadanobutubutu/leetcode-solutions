class Solution:
    def duplicateZeros(self, arr):
        n = len(arr)
        zeros = arr.count(0)

        # 後ろから詰めていく
        i = n - 1
        j = n - 1 + zeros

        while i < j:
            if j < n:
                arr[j] = arr[i]

            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0

            i -= 1
            j -= 1

