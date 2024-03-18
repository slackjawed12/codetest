import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        high = math.sqrt(r2**2 - x**2)
        if x <= r1:
            low = math.sqrt(r1**2 - x**2)
            answer += math.floor(high)-math.ceil(low) + 1
        else:
            answer += math.floor(high)+1
          
    return answer*4