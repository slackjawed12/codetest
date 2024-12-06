from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = 0
        while queue:
            # every loop, ans is set to zero.
            ans = 0
            current_length = len(queue)
            
            for _ in range(current_length):
                node = queue.popleft()
                ans += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 

        # finally, ans is set to leaf node sum by bfs 
        return ans  