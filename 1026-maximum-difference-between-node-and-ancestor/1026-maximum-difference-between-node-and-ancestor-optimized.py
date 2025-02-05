# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = -float('inf')
        def dfs(root, cur_max, cur_min):
            if not root:
                return
            
            cur_max = max(cur_max, root.val)
            cur_min = min(cur_min, root.val)
            self.res = max(self.res, cur_max - cur_min)
            dfs(root.left, cur_max, cur_min)
            dfs(root.right, cur_max, cur_min)
            
        dfs(root, -float('inf'), float('inf'))
        return self.res