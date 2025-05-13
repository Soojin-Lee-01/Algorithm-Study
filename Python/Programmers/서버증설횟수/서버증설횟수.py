def solution(players, m, k):
    answer = 0
    # 리스트로 관리
    # [개수, 시간]
    data = []
    for i in range(len(players)):
        # 시간 감소
        for a in range(len(data)):
            if data[a][1] > 0:
                data[a][1] -= 1
        
        # 몫으로 판별
        if (players[i] // m) >= 1:
            temp = 0
            for j in range(len(data)):
                if data[j][1] > 0:
                    temp += data[j][0]
            if temp > 0:
                if temp < (players[i] // m):
                    temp = (players[i] // m) - temp
                    data.append([temp, k])
            else:
                data.append([players[i]//m, k])
        
    for i in range(len(data)):
        answer += data[i][0]
                
    return answer
