def solution(storey):
    answer = 0
    digit = 10
    while storey > 0:
        r = storey % 10
        if r < 5:
            answer += r
            storey -= r
        elif r > 5:
            answer += 10 - r
            storey += 10 - r
        else:
            nr = (storey // 10) % 10
            if nr >= 5:
                answer += 10-r
                storey += 10-r
            else:
                answer += r
                storey -= r
            
        storey //= 10
        
    return answer