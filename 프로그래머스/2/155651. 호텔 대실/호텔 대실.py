from heapq import heappush, heappop
def solution(book_time):
    converted_time = [[to_num(start), to_num(end)] for start, end in book_time]
    converted_time.sort(key=lambda x:x[0])
    clean_up_time = 10
    heap = []
    answer = 1
    for start, end in converted_time:
        if not heap:
            heappush(heap, end+clean_up_time)
            continue
        
        if heap[0] <= start:
            heappop(heap)
        else:
            answer += 1
        
        heappush(heap, end+clean_up_time)
    
    return answer

def to_num(time_str):
    hour, minute = time_str.split(":")
    return int(hour)*60 + int(minute)