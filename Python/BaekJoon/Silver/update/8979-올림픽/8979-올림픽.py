N, K = map(int, input().split())

data = []
dic = {}

for i in range(N):
    dic[i+1] = []

for i in range(N):
    num = list(map(int, input().split()))
    data.append(num)

data = sorted(data, key=lambda x: (-x[1], -x[2], -x[3]))

count = 1
temp = []
for i in range(len(data)):
    if i == 0:
        data[i].append(count)
    else:
        if data[i][1:4] == data[i-1][1:4]:
            data[i].append(data[i-1][4])

        else:
            data[i].append(count)
    count += 1

for i in range(len(data)):
    if data[i][0] == K:
        print(data[i][4])
