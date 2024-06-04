num = int(input())
one = int(input())
data = []

for i in range(num-1):
    n = int(input())
    data.append(n)

count = 0

if num == 1:
    pass
else:
    while one <= max(data):
        one += 1
        count += 1
        data[data.index(max(data))] -= 1

print(count)