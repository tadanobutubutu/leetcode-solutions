class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            # 右を先に push → 左が先に処理される
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result

