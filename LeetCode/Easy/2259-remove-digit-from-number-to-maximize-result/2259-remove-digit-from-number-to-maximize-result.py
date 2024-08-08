class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = "0"
        for i in range(len(number)):
            if number[i] == digit:
                temp = number[:i]+number[i+1:]
                result = temp if int(temp) > int(result) else result
        
        return result
        