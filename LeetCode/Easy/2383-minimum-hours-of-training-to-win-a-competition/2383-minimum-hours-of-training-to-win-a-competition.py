class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: list[int], experience: list[int]) -> int:
        result = 0
        sum_en = sum(energy)
        result += max(0, sum_en+1-initialEnergy)
       
        acc = initialExperience
        inc_exp = 0
        for e in experience:
            threshold = e + 1
            if acc < threshold:
                inc_exp = max(inc_exp, threshold - acc)
            
            acc += e

        result += inc_exp
        return result           
            