import sys

n = int(sys.stdin.readline())

count = 0
for i in range(n):
    data = sys.stdin.readline().rstrip()
    last = ''
    dic = {}
    for j in range(len(data)):
        if data[j] not in dic:
            dic[data[j]] = 1
            last = data[j]
        else:
            if last != data[j]:
                count -= 1
                break
            dic[data[j]] += 1

    count += 1

print(count)

