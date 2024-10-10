# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        result = None
        return self.helper(root, result)

    def helper(self, root: Optional[TreeNode], result: bool):
        if root is None:
            return result

        if root.val == 1:
            return True
        if root.val == 0:
            return False
        
        is_or = root.val == 2
        l = self.helper(root.left, result)
        r = self.helper(root.right, result)
        
        if is_or:
            return l or r

        return l and r
       
        