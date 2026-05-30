class Solution(object):
    def minOperations(self, nums, k):
        # Even indices must have nums[i] % k == x
        # Odd indices must have nums[i] % k == y
        # We need to find x, y such that x != y to minimize total operations.
        # Operations for a value v to become r mod k:
        # min( (v % k - r) % k, (r - v % k) % k )
        
        n = len(nums)
        def cost(v, r):
            # v % k needs to become r
            # cost = min( (v % k - r) % k, (r - v % k) % k )
            # Wait, this is only true if I can change nums[i] by 1.
            # Yes, increment or decrement by 1.
            # So v % k -> r is min distance.
            rem = v % k
            diff1 = (rem - r) % k
            diff2 = (r - rem) % k
            return min(diff1, diff2)
            
        # Precompute costs for each x in [0, k-1]
        cost_even = [0] * k
        cost_odd = [0] * k
        
        for i in range(n):
            if i % 2 == 0:
                for x in range(k):
                    cost_even[x] += cost(nums[i], x)
            else:
                for y in range(k):
                    cost_odd[y] += cost(nums[i], y)
                    
        min_ops = float('inf')
        for x in range(k):
            for y in range(k):
                if x == y: continue
                min_ops = min(min_ops, cost_even[x] + cost_odd[y])
        return min_ops

