class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        cur = 0
        st = {}
        for i, t in events:
            if i in st:
                st[i] = max(t-cur, st[i])
            else:
                st[i] = t-cur

            cur = t
        
        result = 10**6
        mx = max(st.values())
        for k in st:
            if st[k] == mx:
                result = min(k, result)
            
        return result

            