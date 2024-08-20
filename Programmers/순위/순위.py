def solution(n, results):
    graph = [[0] * n for _ in range(n)]
    
    # 그래프 초기화
    for winner, loser in results:
        graph[winner - 1][loser - 1] = 1
        graph[loser - 1][winner - 1] = -1
    
    # 플로이드-워셜 알고리즘을 사용하여 승패 정보를 전파
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    # i가 j를 이길 수 있는 경우
                    if graph[i][j] == 0:
                        graph[i][j] = 1
                        graph[j][i] = -1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    # i가 j에게 질 수 있는 경우
                    if graph[i][j] == 0:
                        graph[i][j] = -1
                        graph[j][i] = 1
    
    answer = 0
    for i in range(n):
        if graph[i].count(0) == 1:
            answer += 1
    
    return answer
