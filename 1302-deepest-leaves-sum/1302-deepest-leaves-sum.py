# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        leafs = []
        def dfs(root, lev):
            if root is None:
                return
            
            if root.left is None and root.right is None:
                leafs.append((root.val, lev))
            
            dfs(root.left, lev+1)
            dfs(root.right, lev+1)

        dfs(root, 0) 
        mx_lv = -1
        for leaf in leafs:
            mx_lv = max(leaf[1], mx_lv)
        
        result = 0
        for leaf in leafs:
            result += leaf[0] if leaf[1] == mx_lv else 0

        return result
            