from collections import defaultdict 

class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        res = 0
        l = len(nums)
        
        freq = defaultdict()
        # frequency dict init with last two element
        freq[nums[l-1] - nums[l-2]] = 1
        
        for b in range(l - 3, 0, -1):
            # add all frequencies satisfying condition 'nums[a] + nums[b] == nums[d] - nums[c]'
            for a in range(b - 1, -1, -1):
                res += freq[nums[a] + nums[b]]
            
            # update frequencies at index b
            for x in range(l - 1, b, -1):
                freq[nums[x] - nums[b]] += 1
        
        return res