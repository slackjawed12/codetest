class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def sort(lo: int, hi: int):
            if hi <= lo:
                return lo
            
            idx = partition(lo, hi)
            sort(lo, idx-1)
            sort(idx, hi)
        
        def partition(lo:int, hi:int):
            pivot = nums[(lo+hi)//2]
            while lo <= hi:
                while nums[lo] < pivot:
                    lo += 1
                while nums[hi] > pivot:
                    hi -= 1
                
                if lo <= hi:
                    nums[lo], nums[hi] = nums[hi], nums[lo]
                    lo, hi = lo + 1, hi - 1

            return lo
            
        sort(0, len(nums)-1)
    
        
