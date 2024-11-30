class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # pref[0] = arr[0]
        # pref[1] = arr[0] ^ arr[1] -> arr[1] = pref[1] ^ pref[0]
        # pref[2] = arr[0] ^ arr[1] ^ arr[2] -> arr[2] = pref[2] ^ arr[1] ^ arr[0]
        result = []
        result.append(pref[0])
        cur = result[-1]
        for i in range(1, len(pref)):
            result.append(cur ^ pref[i])
            cur = cur ^ result[-1]
        
        return result