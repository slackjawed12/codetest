class Solution:
    def isFascinating(self, n: int) -> bool:
        arr = [0]*10
        for i in range(1,4):
            temp = n*i
            while temp != 0:
                arr[temp%10] += 1
                temp //= 10

        for i, n in enumerate(arr):
            if i == 0 and n != 0:
                return False
            
            if i != 0 and n != 1:
                return False

        return True