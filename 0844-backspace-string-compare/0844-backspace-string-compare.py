class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack, t_stack = self.init(s), self.init(t)
        return s_stack == t_stack
        
    def init(self, s:str) -> List[str]:
        st = []
        for c in s:
            if c == '#':
                if st:
                    st.pop()
            else:
                st.append(c)
        
        return st