# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, res, ancestors):
            if not root:
                return res
            
            ancestors.append(root.val)
            sorted_arr = sorted(ancestors)
            temp = abs(sorted_arr[-1] - sorted_arr[0])
            left_res = dfs(root.left, temp, ancestors)
            right_res = dfs(root.right, temp, ancestors)
            ancestors.pop()
            return max(left_res, right_res)
        
        result = dfs(root, 0, [])
        return result