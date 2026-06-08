# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque()
        queue.append(root)
        height = 0
        while queue:
            n = len(queue)
            for i in range(n):
                r = queue.popleft()
                if r.left: queue.append(r.left)
                if r.right: queue.append(r.right)
            height += 1
        return height




    
