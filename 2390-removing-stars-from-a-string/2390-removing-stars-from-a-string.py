class Solution:
    def removeStars(self, s: str) -> str:
        # leet**cod*e -> f
        st = []
        for c in s:
            if c == '*':
                if st:
                    st.pop()
            else:
                st.append(c)
        
        return "".join(st)
                