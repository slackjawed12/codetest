# 윈도우마다 매번 substr 연산 일어나므로 비효율적
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = len(blocks)
        for i in range(len(blocks)-k+1):
            substr = blocks[i:i+k]
            whites = 0
            for c in substr:
                if c == 'W':
                    whites+=1
            
            result = min(whites, result)
        
        return result


class Solution2:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i, j, nonblack , mn = 0, 0, 0, k 
        while j < len(blocks):
            if blocks[j]== 'W':
                nonblack += 1
            # first time
            if (j - i +1) < k:
                j+=1
            elif (j - i + 1) == k:
                mn = min (mn , nonblack)
                if blocks[i] =='W':
                    nonblack -=1
                i+=1
                j+=1
        return mn
