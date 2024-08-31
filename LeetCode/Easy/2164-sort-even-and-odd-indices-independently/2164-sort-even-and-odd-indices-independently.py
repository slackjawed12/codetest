class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        odds = sorted([num for i, num in enumerate(nums) if i % 2 != 0 ], reverse=True)
        evens = sorted([num for i, num in enumerate(nums) if i % 2 == 0])
        
        result =[evens[i//2] if i % 2 == 0 else odds[i//2] for i, num in enumerate(nums)]
        return result