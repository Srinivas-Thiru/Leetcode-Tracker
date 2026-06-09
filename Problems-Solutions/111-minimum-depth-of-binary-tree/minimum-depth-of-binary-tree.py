# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        level =0
        if not root: return 0
        queue = deque()
        queue.append(root)
        ans = 10**6
        while queue:
            n = len(queue)
            level += 1
            for i in range(n):
                r = queue.popleft()
                if not r.left and not r.right: ans = min(ans, level)
                if r.left: queue.append(r.left)
                if r.right: queue.append(r.right)
        
        return ans
                
