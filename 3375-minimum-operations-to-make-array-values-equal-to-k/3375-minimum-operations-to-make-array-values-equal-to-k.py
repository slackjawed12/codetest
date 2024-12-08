class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        store = set(nums)
        ordered = sorted(list(store))
        result = -1
        while ordered:
            cur = ordered.pop()
            if cur > k:
                if result == -1:
                    result = 1
                else:
                    result += 1
            
        return result
            
            
