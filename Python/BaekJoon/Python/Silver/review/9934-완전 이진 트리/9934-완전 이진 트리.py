import sys

K = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split(' ')))

data = [[] for i in range(K)]

count = 0
def ino(num, count=None):
    if len(num) == 3:
        data[K-2].append(num[1])
        data[K-1].append(num[0])
        data[K-1].append(num[2])
        return
    else:
        data[count].append(num[len(num)//2])
        count += 1
    ino(num[0:len(num) // 2],count)
    ino(num[len(num) // 2 + 1::],count)

ino(num,count)

for i in data:
    print(' '.join(map(str, i)))