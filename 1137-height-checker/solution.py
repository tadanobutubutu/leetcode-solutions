class Solution:
    def heightChecker(self, heights):
        expected = sorted(heights)
        cnt = 0
        for h, e in zip(heights, expected):
            if h != e:
                cnt += 1
        return cnt

