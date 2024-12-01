import heapq

V, E = map(int, input().split())

start = int(input())

graph = {}

for i in range(V):
    graph[i+1] = []

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def solution(graph, start):

    distances = {node: float('inf') for node in graph}

    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_de, new_distance in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_de]:
                distances[new_de] = distance
                heapq.heappush(queue, (distance, new_de))

    return distances


answer = solution(graph, start)

for node in range(1, V + 1):
    if answer[node] == float('inf'):
        print("INF")
    else:
        print(answer[node])
