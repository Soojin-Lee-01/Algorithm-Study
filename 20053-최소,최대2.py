import sys

num = int(sys.stdin.readline())

for i in range(num):
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    print(min(data), max(data))






