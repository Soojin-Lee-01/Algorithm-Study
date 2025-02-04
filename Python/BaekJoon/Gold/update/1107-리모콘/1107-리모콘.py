target = int(input())

num = int(input())

if num == 0:
    data = []
else:
    data = list(map(int, input().split()))

min_num = abs(target - 100)

for i in range(500000):
    temp = str(i)
    for n in temp:
        if int(n) in data:
            break
    else:
        min_num = min(min_num, abs(target - i) + len(temp))
print(min_num)
