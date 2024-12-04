# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def search(root, cur_sum):
            if root is None:
                return cur_sum

            right_sum = search(root.right, cur_sum)
            root.val += right_sum
            return search(root.left, root.val)

        search(root, 0)
        return root