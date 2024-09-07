class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        result = 0
        for x in range(len(strs[0])):
            is_sorted = True
            for y in range(len(strs)-1):
                cur, n = strs[y][x], strs[y+1][x]
                if ord(cur) > ord(n):
                    is_sorted = False
                    break
            
            if not is_sorted:
                result += 1

        return result
