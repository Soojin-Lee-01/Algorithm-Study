n, m = map(int, input().split(' '))

data = []

for i in range(n):
    word = list(map(str, input().rstrip()))
    data.append(word)

result = ''
count = 0

dic = {}
for i in range(m):
    for j in range(n):
        if data[j][i] in dic:
            dic[data[j][i]] += 1
        elif data[j][i] not in dic:
            dic[data[j][i]] = 1
    ma = 0
    tem = []
    for j in dic:
        tem.append([j, dic[j]])
    tem = sorted(tem,key=lambda x: (-x[1], x[0]))
    result += tem[0][0]
    for j in dic:
        if j != tem[0][0]:
            count += dic[j]
    dic = {}

print(result)
print(count)