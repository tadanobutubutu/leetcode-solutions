class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        
        q = deque([root])
        res = []
        
        while q:
            level_sum = 0
            size = len(q)
            
            for _ in range(size):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level_sum / size)
        
        return res

