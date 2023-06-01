def solution(arr, queries):
    answer = arr
    for query in queries:
        temp = arr[query[0]]
        arr[query[0]] = arr[query[1]]
        arr[query[1]] = temp
        
    return answer