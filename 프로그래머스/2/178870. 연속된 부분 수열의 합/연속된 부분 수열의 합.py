def solution(sequence, k):
    answer = []
    
    cur_sum = sequence[0]
    left, right = 0, 0
    while right < len(sequence) and left < len(sequence):
        if cur_sum == k:
            if len(answer) == 0:
                answer = [left, right]
            elif answer[1] - answer[0] > right-left:
                answer = [left, right]
            elif answer[0] > left:
                answer = [left, right]
            right += 1
            if right < len(sequence):
                cur_sum += sequence[right]
            cur_sum -= sequence[left]
            left += 1
        elif cur_sum > k:
            cur_sum -= sequence[left]
            left += 1
        else:
            right += 1
            if right < len(sequence):
                cur_sum += sequence[right]
            
    return answer