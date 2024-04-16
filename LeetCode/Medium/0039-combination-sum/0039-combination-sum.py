class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        return self.combinationSumHelper(candidates, 0, target, [], [])
    def combinationSumHelper(self, candidates: list[int], idx:int, target:int, cur:list[int], result: list[list[int]]):
        if sum(cur) > target:
            return result

        if sum(cur) == target:
            result.append(cur[:])
            return result
        
        for i in range(idx, len(candidates)):
            cur.append(candidates[i])
            result = self.combinationSumHelper(candidates, i, target, cur, result)
            cur.pop()
        
        return result
        
        

        
