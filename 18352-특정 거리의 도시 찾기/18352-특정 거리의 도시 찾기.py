import heapq
import sys

# 다익스트라 알고리즘을 사용한 풀이

N, M, K, X = map(int, sys.stdin.readline().split(' '))
graph = {}
for i in range(N):
    graph[i+1] = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append((1,b))

costs = {}
pq = []
heapq.heappush(pq, (0, X))

while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    if cur_node not in costs:
        costs[cur_node] = cur_cost
        for cost, next_node in graph[cur_node]:
            next_cost = cur_cost + cost
            heapq.heappush(pq, (next_cost, next_node))


for node in range(1, N+1):
    if node not in costs:
        costs[node] = -1
result = []
for i in range(1, len(costs)+1):
    if costs[i] == K:
        result.append(i)
result.sort()

if len(result) > 0:
    for i in result: print(i)
else:
    print(-1)

