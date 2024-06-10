import sys

dic = {}
count = 0
while True:
    data = sys.stdin.readline().rstrip()
    if data == '':
        break
    count += 1
    if data in dic:
        dic[data] += 1
    elif data not in dic:
        dic[data] = 1

result = []
for i in dic:
    result.append((i, dic[i]))

result = sorted(result)

for x, y in result:
    print(x , '{:.4f}'.format(y/count*100))