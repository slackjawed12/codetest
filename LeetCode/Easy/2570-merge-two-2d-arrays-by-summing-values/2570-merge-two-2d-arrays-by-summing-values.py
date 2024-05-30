tclass Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        store = {i:val for i, val in nums1}
        for i, val in nums2:
            if i in store:
                store[i] += val
            else:
                store[i] = val
        
        return sorted(list(store.items()), key=lambda x: x[0])