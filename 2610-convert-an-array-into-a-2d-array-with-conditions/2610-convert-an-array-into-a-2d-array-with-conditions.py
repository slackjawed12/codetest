class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []
        for n in nums:
            insert = False
            for prev in result:
                if n not in prev:
                    prev.add(n)
                    insert = True
                    break
            if not insert:
                result.append(set([n]))
                    
        return [list(row) for row in result]
        