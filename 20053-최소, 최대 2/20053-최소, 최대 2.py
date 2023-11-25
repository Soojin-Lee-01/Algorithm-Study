import sys

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    print(min(num), end=' ')
    print(max(num))