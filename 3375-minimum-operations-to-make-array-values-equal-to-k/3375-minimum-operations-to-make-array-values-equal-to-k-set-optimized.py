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
            elif cur == k:
                if ordered:
                    return -1
                else:
                    return 0 if result < 0 else result
            else:
                return -1
            
        return result
            
            
