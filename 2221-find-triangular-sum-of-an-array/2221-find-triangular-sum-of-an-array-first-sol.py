class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        sums = nums
        while len(sums) != 1:
            tmp = []
            for i in range(len(sums)-1):
                tmp.append((sums[i]+sums[i+1])%10)
            
            sums = tmp
        
        return sums[0]

                
                    
