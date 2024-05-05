class Solution:
    def trimMean(self, arr: list[int]) -> float:
        sorted_arr = sorted(arr)
        filtered = sorted_arr[len(arr)//20:-len(arr)//20]
        return sum(filtered)/len(filtered)