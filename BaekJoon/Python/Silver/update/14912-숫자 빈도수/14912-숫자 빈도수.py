n, m = map(int, input().split(' '))

result = 0

for i in range(1, n+1):
    data = list(str(i))
    for j in range(len(data)):
        if data[j] == str(m):
            result += 1

print(result)