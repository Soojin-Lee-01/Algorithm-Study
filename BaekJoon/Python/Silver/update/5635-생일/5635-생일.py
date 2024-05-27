temp = []

n = int(input())

for i in range(n):
    data = list(map(str, input().split(' ')))
    temp.append(data)

for i in range(n):
    temp[i][1] = int(temp[i][1])
    temp[i][2] = int(temp[i][2])
    temp[i][3] = int(temp[i][3])

temp = sorted(temp, key=lambda x: (x[3], x[2], x[1]), reverse=True)

print(temp[0][0])
print(temp[len(temp)-1][0])