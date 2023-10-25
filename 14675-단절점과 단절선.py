import sys

N = int(sys.stdin.readline())

graph = {}

for i in range(N):
    graph[i+1] = []

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[a].append(b)
    graph[b].append(a)

q = int(sys.stdin.readline())

for i in range(q):
    m , l = map(int, sys.stdin.readline().split(' '))
    if m == 1:
        if len(graph[l]) < 2:
            print("no")
        else:
            print("yes")
    else:
        print("yes")


