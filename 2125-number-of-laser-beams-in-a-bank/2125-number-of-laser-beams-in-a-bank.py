class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        def count_one(arr):
            return len([c for c in arr if c == '1'])
        counts = [count_one(row) for row in bank]
        non_zero = [num for num in counts if num]
        if len(non_zero) <= 1:
            return 0
        
        result = 0
        for i in range(len(non_zero)-1):
            result += non_zero[i]*non_zero[i+1]
        
        return result
            