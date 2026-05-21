class Solution:
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False

        i = 0

        # 上り
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # 山頂が端ならダメ
        if i == 0 or i == n - 1:
            return False

        # 下り
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1

