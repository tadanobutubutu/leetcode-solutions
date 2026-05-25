class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Convert list to array
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(arr[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node
        
        return build(0, len(arr) - 1)

