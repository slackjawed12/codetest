class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        result = []
        for i in range(m):
            s, e = l[i], r[i]
            seq = nums[s:e+1]
            result.append(self.arithmetic(seq))

        return result
    
    def arithmetic(self, arr:List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != d:
                return False
        
        return True
