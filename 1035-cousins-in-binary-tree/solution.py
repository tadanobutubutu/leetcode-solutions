class Solution:
    def isCousins(self, root, x, y):
        from collections import deque
        q = deque([(root, None)])  # (node, parent)

        while q:
            size = len(q)
            px = py = None  # parents of x and y

            for _ in range(size):
                node, parent = q.popleft()

                if node.val == x:
                    px = parent
                if node.val == y:
                    py = parent

                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

            # 同じレベルで見つかったら判定
            if px and py:
                return px != py  # 親が違えばいとこ
            # 片方だけ見つかったら同じレベルにいない
            if px or py:
                return False

        return False

