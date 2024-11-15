# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        result = set(self.search(root, []))
        return -1 if len(result) <= 1 else sorted(result)[1]
        
    
    def search(self, root:Optional[TreeNode], result: List[int]) -> List[int]:
        if root is None:
            return result
        
        result.append(root.val) 
        result = self.search(root.left, result)
        result = self.search(root.right, result)
        return result
        