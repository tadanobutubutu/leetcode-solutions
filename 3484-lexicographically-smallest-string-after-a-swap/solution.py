class Solution:
    def getSmallestString(self, s: str) -> str:
        arr = list(s)
        for i in range(len(arr) - 1):
            d1 = int(arr[i])
            d2 = int(arr[i + 1])
            if (d1 % 2 == d2 % 2) and d1 > d2:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                break
        return "".join(arr)

