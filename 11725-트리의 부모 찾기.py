import sys
from collections import deque

n = int(sys.stdin.readline()) # 노드의 개수
graph = {} # 인접 리스트 생성
for i in range(n):
    graph[i + 1] = []

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b) # 양방향 연결
    graph[b].append(a)

visited = [False] * (n + 1) # 각 노드의 방문 여부를 나타냄
parents = [0] * (n + 1) # 각 노드의 부모를 저장

queue = deque()
queue.append(1) # 1번 노드에서 시작

while queue:
    node = queue.popleft()
    visited[node] = True

    for child in graph[node]: # 자식노드를 순회
        if not visited[child]: # 방문하지 않은 자식이면
            parents[child] = node # 자식 노드의 부모를 현재 노드로
            queue.append(child) # 큐에 자식노드 추가

for i in range(2, n + 1): # 2번 노드부터 부모노드 출력
    print(parents[i])