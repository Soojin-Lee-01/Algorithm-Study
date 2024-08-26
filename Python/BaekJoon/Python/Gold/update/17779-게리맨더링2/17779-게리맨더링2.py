N = int(input())

graph = [[]]

for _ in range(N):
    data = list(map(int, input().split()))
    graph.append([0] + data)

def cal(x, y, d1, d2):
    count = [0 for _ in range(5)]

    temp_graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

    # 5번 구역 경계선 설정
    for i in range(d1+1):
        temp_graph[x+i][y-i] = 1
        temp_graph[x+d2+i][y+d2-i] = 1
    for j in range(d2 + 1):
        temp_graph[x+j][y+j] = 1
        temp_graph[x+d1+j][y-d1+j] = 1

    # 5번 구역 경계선 기준으로 내부 채우기
    for i in range(x+1, x+d1+d2):
        flag = False
        for j in range(N+1):
            if temp_graph[i][j] == 1:
                if flag == True:
                    flag = False
                else:
                    flag = True
            else:
                if flag == True:
                    temp_graph[i][j] = 1

    for i in range(1, N+1):
        for j in range(1, N+1):
            # 만약 1번 구역이라면 더해주기
            if i < x + d1 and j <= y and temp_graph[i][j] != 1:
                count[0] += graph[i][j]
            # 만약 2번 구역이라면 더해주기
            elif i <= x + d2 and y < j and temp_graph[i][j] != 1:
                count[1] += graph[i][j]
            # 만약 3번 구역이라면 더해주기
            elif x + d1 <= i and j < y - d1 + d2 and temp_graph[i][j] != 1:
                count[2] += graph[i][j]
            # 만약 4번 구역이라면 더해주기
            elif x + d2 < i and y - d1 + d2 <= j and temp_graph[i][j] != 1:
                count[3] += graph[i][j]
            # 만약 5번 구역이라면 더해주기
            elif temp_graph[i][j] == 1:
                count[4] += graph[i][j]
    # 최댓값과 최솟값 차이
    return max(count) - min(count)

answer = float('inf')

for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if 1 <= x < x + d1 + d2 <= N and 1 <= y-d1 < y < y+ d2 <= N:
                    # 가장 최솟값 구하기
                    answer = min(answer, cal(x, y, d1, d2))

print(answer)
