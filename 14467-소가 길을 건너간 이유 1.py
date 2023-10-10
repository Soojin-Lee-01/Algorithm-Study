import sys

N = int(sys.stdin.readline())

count = 0
graph = {}
rount = {}

for i in range(10):
    graph[i+1] = 2
    rount[i+1] = []

for i in range(N):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    rount[a[0]] = a[1]

    if graph[a[0]] == 2:
        graph[a[0]] = a[1]
        continue
    elif graph[a[0]] != a[1]:
        count += 1
        graph[a[0]] = a[1]
print(count)

