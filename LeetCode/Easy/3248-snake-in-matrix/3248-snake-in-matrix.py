class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        result = 0
        for d in commands:
            if d == 'DOWN':
                result += n
            elif d == 'UP':
                result -= n
            elif d == 'RIGHT':
                result += 1
            else:
                result -= 1
        
        return result