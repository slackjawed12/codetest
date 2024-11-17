class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        l = len(nums)
        acc, acc_r = [0]*l, [0]*l
        
        for i, n in enumerate(nums):
            acc[i] += acc[i-1]+n
        
        for i, n in enumerate(reversed(nums)):
            acc_r[l-i-1] += n if i ==0 else acc_r[l-i] + n
        print(acc, acc_r)
        result = 0
        for i, n in enumerate(nums):
            if n == 0:
                if acc[i] == acc_r[i]:
                    result += 2
                elif abs(acc[i] - acc_r[i]) == 1:
                    result += 1
                
        return result