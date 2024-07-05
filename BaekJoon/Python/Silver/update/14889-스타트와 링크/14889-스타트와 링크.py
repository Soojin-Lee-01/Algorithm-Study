from collections import deque

n = int(input())

graph = []

for i in range(n):
    data = list(map(int, input().split(" ")))
    graph.append(data)

result = []
person = [i for i in range(1, n+1)]
#이제 조합을 구해보자!
def combination(n, start = 0, combo = []):
    if len(combo) == n:
        result.append(combo[:])
        return
    for i in range(start, len(person)):
        combo.append(person[i])
        combination(n, i+1, combo)
        combo.pop()

combination(n//2)
result = deque(result)

final = 10e9
while len(result) > 0:
    temp = result.popleft()
    data1 = temp
    data2 = []
    for k in range(1, n+1):
        if k not in data1:
            data2.append(k)
    data1_sum = 0
    for a in range(0, len(data1)):
        for b in range(a, len(data1)):
            data1_sum += graph[data1[a]-1][data1[b]-1]
            data1_sum += graph[data1[b]-1][data1[a]-1]
    data2_sum = 0
    for a in range(0, len(data2)):
        for b in range(a, len(data2)):
            data2_sum += graph[data2[a]-1][data2[b]-1]
            data2_sum += graph[data2[b]-1][data2[a]-1]
    final = min(abs(data1_sum-data2_sum), final)


print(final)
