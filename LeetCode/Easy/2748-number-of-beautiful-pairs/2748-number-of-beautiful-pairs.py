class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        answer = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                first_digit = int(str(nums[i])[0])
                last_digit = int(str(nums[j])[-1])
                digit_gcd = self.gcd(first_digit, last_digit)
                if digit_gcd == 1:
                    answer += 1
        
        return answer
    
    def gcd(self, a, b):
        if b == 0:
            return a
        
        return self.gcd(b, a%b)
                