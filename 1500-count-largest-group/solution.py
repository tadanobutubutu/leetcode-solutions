from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
            
        groups = Counter(digit_sum(i) for i in range(1, n + 1))
        max_size = max(groups.values())
        return sum(1 for size in groups.values() if size == max_size)

