class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        result = []
        carry = 0
        i = len(num)-1
        while k:
            digit = k % 10
            added = digit + carry
            r = num[i] + added if i >= 0 else added
            carry = 1 if r >= 10 else 0
            if i < 0:
                result.append(r if r < 10 else r - 10)
            else:
                num[i] = r if r < 10 else r - 10
                i -= 1

            k //= 10
        
        while i >= 0:
            r = num[i] + carry
            num[i] = r if r < 10 else r - 10
            carry = 1 if r >= 10 else 0
            i -= 1

        if carry:     
            result.append(carry)
            
        result.reverse()
        return result + num