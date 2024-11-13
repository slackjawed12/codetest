import heapq
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i, n in enumerate(nums):
            l = [n for j, n in enumerate(nums) if j != i]
            is_inc = True
            for k in range(1,len(l)):
                if l[k-1] >= l[k]:
                    is_inc = False
                    break

            if is_inc:
                return True
        
        return False
