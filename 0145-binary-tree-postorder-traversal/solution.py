class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        # 逆順にすることで後順になる
        return result[::-1]

