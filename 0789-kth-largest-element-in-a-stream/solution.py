import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # ヒープのサイズを k に保つ
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # k 個より多くなったら最小を捨てる
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

