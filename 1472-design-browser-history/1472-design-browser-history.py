class BrowserHistory:
    homepage = ''
    back_st = []
    forward_st = []

    def __init__(self, homepage: str):
        self.back_st = []
        self.forward_st = []
        self.homepage = homepage

    def visit(self, url: str) -> None:
        self.back_st.append(url)
        self.forward_st= []

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.back_st:
                self.forward_st.append(self.back_st.pop())

        if not self.back_st:
            return self.homepage
        
        return self.back_st[-1]

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.forward_st:
                self.back_st.append(self.forward_st.pop())
        
        if not self.back_st:
            return self.homepage

        return self.back_st[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)