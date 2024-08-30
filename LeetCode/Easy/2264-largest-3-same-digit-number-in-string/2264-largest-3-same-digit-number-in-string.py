class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""
        for i in range(len(num)-2):
            substr = num[i:i+3]
            if not self.isGood(substr):
                continue

            if result == "" or result == "000":
                result = substr
            else:
                mx = max(int(substr), int(result))
                result = str(mx)

        return result
    
    def isGood(self, s:str)->bool:
        return s[0] == s[1] and s[1] == s[2]