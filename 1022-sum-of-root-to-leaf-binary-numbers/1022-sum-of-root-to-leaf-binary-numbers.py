# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0, 0)
        
    def helper(self, root: Optional[TreeNode], cur: int, result: int) -> int:
        if root is None:
            return result
        
        if root.left is None and root.right is None:
            result += (cur << 1) + root.val
            return result
        
        l = self.helper(root.left, (cur << 1) + root.val, result) 
        r  = self.helper(root.right, (cur << 1) + root.val, result)
        return l+r