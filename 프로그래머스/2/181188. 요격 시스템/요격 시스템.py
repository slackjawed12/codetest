def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    criteria = targets[0]
    answer += 1
    for cur in targets:
        if criteria[1] <= cur[0]:
            answer+=1
            criteria=cur
            
    return answer