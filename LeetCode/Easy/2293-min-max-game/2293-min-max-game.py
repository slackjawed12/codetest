class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        temp = nums
        while len(temp) > 1:
            new = []
            for i in range(len(temp)//2):
                if i % 2 ==0:
                    new.append(min(temp[2*i], temp[2*i+1]))
                else:
                    new.append(max(temp[2*i], temp[2*i+1]))
            
            temp = new

        return temp[0]

                