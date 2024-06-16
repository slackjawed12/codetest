class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        lowers = set('abcdefghijklmnopqrstuvwxyz')
        uppers = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        digits = set('1234567890')
        specials = set('!@#$%^&*()-+')
        p = set(password)
        if not lowers & p:
            return False

        if not uppers & p:
            return False

        if not digits & p:
            return False

        if not specials & p:
            return False
        
        prev = password[0]
        for cur in password[1:]:
            if prev == cur :
                return False
            prev = cur 

        return True
