n, k = map(int, input().split(' '))
result = []
data = []
dic = {}
for i in range(1, n + 1):
    dic[i] = 0
for i in range(1, n + 1):
    data.append(i)
temp = k - 1

while len(data) != 1:
    result.append(data[temp])
    data.remove(data[temp])

    temp += k - 1
    if temp != 0:
        temp = temp % len(data)
result.append(data[0])
print("<" + ', '.join(map(str, result)) + ">")