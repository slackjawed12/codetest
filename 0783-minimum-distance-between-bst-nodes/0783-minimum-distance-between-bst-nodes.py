# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        elem = []
        def search(root):
            if not root:
                return
            
            elem.append(root.val)
            search(root.left)
            search(root.right)
        
        search(root)
        elem.sort()
        result = 999999999
        for i in range(1,len(elem)):
            result = min(result, elem[i]-elem[i-1])
        
        return result
            