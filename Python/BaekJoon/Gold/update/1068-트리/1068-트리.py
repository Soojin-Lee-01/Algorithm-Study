from collections import deque

N = int(input())

data = list(map(int, input().split()))

target = int(input())

# 그래프 구성
graph = {}

# 초기 그래프
for i in range(N):
    graph[i] = []

# 트리 구성
for i in range(len(data)):
    if data[i] != -1:
        graph[data[i]].append(i)

temp = [target]

for i in graph:
    if target in graph[i]:
        temp = []
        for j in graph[i]:
            if j != target:
                temp.append(j)
        graph[i] = temp

# BFS로 풀자
def bfs(start):
    queue = deque()
    queue.append(start)
    temp_num = set()
    temp_num.add(start)
    visited = [False for _ in range(N+1)]
    visited[start] = True

    while queue:
        cur_r = queue.popleft()

        for v in graph[cur_r]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                temp_num.add(v)

    return temp_num

result_target = bfs(target)
result = 0

for i in graph:
    if i not in result_target:
        if len(graph[i]) == 0:
            result += 1

print(result)
