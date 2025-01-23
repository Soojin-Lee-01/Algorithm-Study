from collections import deque

n, m = map(int, input().split())

data = list(map(int, input().split()))

answer = [0 for _ in range(n)]

for i in range(len(data)):
    temp = -1
    for j in range(len(answer)):
        if answer[j] == data[i]:
            temp = j
    if temp == -1:
        for k in range(len(answer)-1, 0, -1):
            answer[k] = answer[k-1]
    else:
        for k in range(temp, 0, -1):
            answer[k] = answer[k-1]
    answer[0] = data[i]

print(" ".join(map(str, answer)))
