def solution(sizes):
    w = []
    h = []
    
    # 가장 큰 수 따로, 가장 작은 수 따로 넣고 그 중 가장 큰 수끼리 곱하기 
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])
    
    return max(w) * max(h)
