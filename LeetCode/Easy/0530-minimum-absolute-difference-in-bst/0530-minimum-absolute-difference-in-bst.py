from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = self.traverse(root, [])
        nums.sort()
        result = nums[1]-nums[0]
        for i in range(1, len(nums)):
            result = min(nums[i]-nums[i-1], result)
            
        return result
    
    def traverse(self, root: Optional[TreeNode], result: List[int]) -> List[int]:
        if root is None:
            return result
        
        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)
        return result
