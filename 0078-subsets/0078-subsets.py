class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(nums, idx, cur):
            result.append(cur[:])
            for i in range(idx+1, len(nums)):
                cur.append(nums[i])
                dfs(nums, i, cur)
                cur.pop()
        
        dfs(nums, -1, [])
        return result
