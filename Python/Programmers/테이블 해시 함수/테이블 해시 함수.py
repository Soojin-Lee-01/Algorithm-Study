def solution(data, col, row_begin, row_end):
    answer = []
    
    data = sorted(data, key=lambda x : (x[col-1], -x[0]))
    
    for i in range(row_begin, row_end+1):
        temp = data[i-1]
        final = 0
        for j in range(len(temp)):
            final += temp[j] % i
        answer.append(final)
    res = answer[0]
    for i in range(1, len(answer)):
        res ^= answer[i]
    
    return res
