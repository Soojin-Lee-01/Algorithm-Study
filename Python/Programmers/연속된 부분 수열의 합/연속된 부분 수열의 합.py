def solution(sequence, k):
    answer = []
    left = 0
    right = 1
    
    if len(sequence) == 1 or sequence[0] == k:
        if sequence[0] == k:
            return [0, 0]
    else:
        sum_n = sequence[0] + sequence[1]
        while True:
            if left == len(sequence)-1 and right == len(sequence)-1:
                if sequence[left] == k:
                    answer.append((left, right, right - left))
                break
            if sum_n < k:
                if right < len(sequence)-1:
                    right += 1
                    sum_n += sequence[right]
                else:
                    left += 1
                    sum_n -= sequence[left-1]
            elif sum_n > k:
                left += 1
                sum_n -= sequence[left-1]
            else:
                answer.append((left, right, right - left))
                if right < len(sequence)-1:
                    right += 1
                    sum_n += sequence[right]
                else:
                    left += 1
                    sum_n -= sequence[left-1]
                    
        answer = sorted(answer, key=lambda x: (x[2], x[0], x[1]))
        
                   
    return answer[0][:2]
