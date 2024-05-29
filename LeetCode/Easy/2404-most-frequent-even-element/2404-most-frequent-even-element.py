class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        even_counts = {}
        for num in nums:
            if num % 2 == 0:
                if num not in even_counts:
                    even_counts[num] = 1
                else:
                    even_counts[num] += 1

        if not even_counts:
            return -1
        
        sorted_counts = list(even_counts.items())
        sorted_counts.sort(key=lambda x:(-x[1], x[0]))
        return sorted_counts[0][0]