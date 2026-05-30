class Solution(object):
    def countValidSubsets(self, parent, nums, k):
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
        MOD = 10**9 + 7
        def dfs(u):
            dp_not_picked = [0] * k
            dp_picked = [0] * k
            dp_not_picked[0] = 1
            dp_picked[nums[u] % k] = 1
            for v in adj[u]:
                res_not_picked_v, res_picked_v = dfs(v)
                next_dp_not_picked = [0] * k
                next_dp_picked = [0] * k
                for r1 in range(k):
                    if dp_not_picked[r1] == 0: continue
                    for r2 in range(k):
                        total_v = (res_not_picked_v[r2] + res_picked_v[r2]) % MOD
                        rem = (r1 + r2) % k
                        next_dp_not_picked[rem] = (next_dp_not_picked[rem] + dp_not_picked[r1] * total_v) % MOD
                for r1 in range(k):
                    if dp_picked[r1] == 0: continue
                    for r2 in range(k):
                        rem = (r1 + r2) % k
                        next_dp_picked[rem] = (next_dp_picked[rem] + dp_picked[r1] * res_not_picked_v[r2]) % MOD
                dp_not_picked = next_dp_not_picked
                dp_picked = next_dp_picked
            return dp_not_picked, dp_picked
        res_not_picked, res_picked = dfs(0)
        return (res_not_picked[0] + res_picked[0] - 1) % MOD

