import sys

n = int(sys.stdin.readline())
num = int(sys.stdin.readline())

graph = [[2,3],[1,4]]

for i in range(3, n+1):
    if i % 2 == 0:
        graph.insert(0, [])
        for j in range(i):
            graph[0].append(graph[1][0] + (j+1))
        for j in range(i-1):
            graph[j+1].append(graph[0][i-1] + (j+1))
    else:
        for k in range(i-1):
            graph[k].insert(0, i**2 - k)
        graph.append([])
        for k in range(i):
            graph[i-1].append(graph[i-2][0] - (k+1))


for i in range(n):
    print(' '.join(map(str, graph[i])))
for i in range(n):
    for j in range(n):
        if graph[i][j] == num:
            print(i+1, j+1)
