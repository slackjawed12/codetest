# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        idx, mx = 0, 0
        for i in range(len(nums)):
            if nums[i] >= mx:
                idx = i
                mx = nums[i]
            
        result = TreeNode(mx, None, None)
        result.left = self.constructMaximumBinaryTree(nums[:idx])
        result.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return result