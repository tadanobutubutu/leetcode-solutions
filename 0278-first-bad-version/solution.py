# The API isBadVersion is defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid   # mid も bad なので右側を縮める
            else:
                left = mid + 1  # mid は good なので左側を進める
        return left

