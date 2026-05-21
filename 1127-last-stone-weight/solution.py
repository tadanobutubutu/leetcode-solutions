import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Python は最小ヒープなので、負にして最大ヒープ化
        h = [-s for s in stones]
        heapq.heapify(h)

        while len(h) > 1:
            y = -heapq.heappop(h)  # 最大
            x = -heapq.heappop(h)  # 2番目に大きい

            if y != x:
                heapq.heappush(h, -(y - x))

        return -h[0] if h else 0

