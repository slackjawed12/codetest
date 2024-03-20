def solution(plans):
    answer = []
    converted = [(work[0], to_time(work[1]), int(work[2])) for work in plans]
    converted.sort(key=lambda x: x[1])
    stack = []
    for i in range(len(converted)-1):
        name, start, work_time = converted[i]
        stack.append((name,work_time))
        time_gap = converted[i+1][1] - start
        while stack and time_gap>0:
            last = stack.pop()
            name, left_time = last
            if left_time <= time_gap:
                time_gap -= left_time
                answer.append(last[0])
            else:
                stack.append((name, left_time-time_gap))
                time_gap = 0
    
    answer.append(converted[-1][0])
    while stack:
        work = stack.pop()
        answer.append(work[0])
        
    return answer

def to_time(start:str):
    hour, minute = start.split(":")
    return int(hour) * 60 + int(minute)