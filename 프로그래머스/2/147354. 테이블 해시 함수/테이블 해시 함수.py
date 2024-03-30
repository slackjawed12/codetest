def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    answer = 0
    for i in range(row_begin, row_end+1):
        s_i = 0
        for j in range(len(data[i-1])):
        	s_i += data[i-1][j] % i
            
        answer = answer ^ s_i
        
    return answer