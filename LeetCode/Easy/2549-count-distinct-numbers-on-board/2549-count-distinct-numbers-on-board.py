# Time - O(n^2), Space - O(n^2)
class SolutionOne:
    def distinctIntegers(self, n: int) -> int:
        board = {n}
        
        while True:
            new_nums = {i for x in board for i in range(1, n+1) if x % i == 1}

            if new_nums.issubset(board):
                break
            
            board |= new_nums
        
        return len(board)


# optimized solution
class SolutionTwo:
    def distinctIntegers(self, n: int) -> int:
        return max(n-1, 1)