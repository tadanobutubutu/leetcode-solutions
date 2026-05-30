import math

class Solution(object):
    def countKthRoots(self, l, r, k):
        # We need to count x such that l <= x^k <= r.
        # This is equivalent to x such that l^(1/k) <= x <= r^(1/k).
        # x is an integer, so ceil(l^(1/k)) <= x <= floor(r^(1/k)).
        
        # Power is at most 10^9, so x^k <= 10^9.
        # x <= (10^9)^(1/k) = 10^(9/k).
        # For k=1, x <= 10^9.
        # For k=30, x <= 10^(9/30) = 10^0.3 approx 2.
        
        if k == 1:
            return max(0, r - l + 1)
        
        # Calculate x_min and x_max
        x_min = math.ceil(pow(l, 1.0/k))
        # Need to be careful with floating point precision.
        # A more robust way is to binary search for x.
        
        def get_root_floor(n, k):
            # Find largest x such that x^k <= n
            if n < 0: return -1
            if n == 0: return 0
            low = 0
            high = int(pow(n, 1.0/k)) + 2
            ans = 0
            while low <= high:
                mid = (low + high) // 2
                if mid == 0:
                    low = 1
                    continue
                if pow(mid, k) <= n:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        
        # Number of perfect k-th powers <= r is get_root_floor(r, k) + 1 (including 0 if 0 is included)
        # Wait, the problem says l, r >= 0. Perfect powers are x^k. 0^k is 0. 1^k is 1.
        # Let's count perfect powers in [l, r] as count(r) - count(l-1)
        
        def count_upto(n, k):
            if n < 0: return 0
            return get_root_floor(n, k) + 1
            
        return count_upto(r, k) - count_upto(l - 1, k)


