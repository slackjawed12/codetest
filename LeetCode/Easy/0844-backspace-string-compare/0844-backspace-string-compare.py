class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t) -1
        ci, cj = i, j
        while i >= 0 or j >= 0:
            ci = self.next(s, i)
            cj = self.next(t, j)
            if ci < 0 or cj < 0:
                return ci < 0 and cj < 0
            elif s[ci] != s[cj]:
                return False

            i = ci - 1
            j = cj - 1

        return True
        
    def next(self, s:str, i:int) -> int:
        if i < 0:
            return - 1
        
        back_cnt = 0
        while i > 0:
            cur = s[i]
            if cur != '#' and back_cnt == 0:
                break

            if cur == '#':
                back_cnt += 1
            else:
                back_cnt -= 1
        
            i -= 1

        return i