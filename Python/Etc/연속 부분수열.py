N, M = map(int, input().split())
data = list(map(int, input().split()))

p2 = 0
temp = 0
answer = 0

for i in range(N):
    temp += data[i]
    if temp == M: answer += 1
    while (temp >= M):
        temp -= data[p2]
        p2 += 1
        if temp == M: answer += 1

print(answer)
