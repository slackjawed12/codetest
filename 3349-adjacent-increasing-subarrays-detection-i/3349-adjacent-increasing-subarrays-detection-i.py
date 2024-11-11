class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        idx = []
        i, j = 0, 0
        while j + 1 < len(nums):
            if nums[j] < nums[j+1]:
                if j - i + 2 == k:
                    idx.append(i)
                    i += 1
            else:
                i = j+1

            j += 1 

        store = set(idx)
        for n in idx:
            if n - k in store:
                return True
        
        return False