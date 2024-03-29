import sys

n, k = map(int, sys.stdin.readline().split())
after = list(map(int, sys.stdin.readline().rstrip().split()))
d = list(map(int, sys.stdin.readline().rstrip().split()))

result = list(range(n))

graph = [-1] * n

for i in range(k):
    temp = [0] * n
    for j in range(n):
        temp[d[j] - 1] = result[j]
    result = temp.copy()

final = [after[result[i]] for i in range(n)]

for i in final:
    print(i, end=' ')
