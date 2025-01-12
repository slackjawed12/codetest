# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root, h):
            if not root:
                return (True, h)
            
            l = helper(root.left, h+1)
            r = helper(root.right, h+1)
            return (l[0] and r[0] and abs(l[1]-r[1]) <= 1, max(l[1], r[1]))

        return helper(root, 0)[0]
    