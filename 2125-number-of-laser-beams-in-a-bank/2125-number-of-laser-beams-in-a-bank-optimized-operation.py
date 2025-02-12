class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev = 0
        for row in bank:
            cnt = row.count('1')
            if cnt == 0:
                continue
            result += prev * cnt
            prev = cnt
        return result   
