n = int(input())

end = 0
result = 0

data = []

for i in range(n):
    a, b = map(int, input().split(' '))
    data.append([a, b])

data = sorted(data, key=lambda x: (x[1], x[0]))

for new_x, new_y in data:
    if end <= new_x:
        result += 1
        end = new_y

print(result)