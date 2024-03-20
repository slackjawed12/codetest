def solution(plans):
    plans = sorted(map(lambda x: [x[0], int(x[1][:2]) * 60 + int(x[1][3:]), int(x[2])], plans), key=lambda x: -x[1])

    lst = []
    while plans:
        x = plans.pop()
        for i, v in enumerate(lst):
            prev_end_time = v[0]
            end_time = x[1]+x[2]
            if v[0] > x[1]:
                lst[i][0] += x[2]
        lst.append([x[1] + x[2], x[0]])
    lst.sort()

        
    return [l[1] for l in lst]

def to_time(start:str):
    hour, minute = start.split(":")
    return int(hour) * 60 + int(minute)