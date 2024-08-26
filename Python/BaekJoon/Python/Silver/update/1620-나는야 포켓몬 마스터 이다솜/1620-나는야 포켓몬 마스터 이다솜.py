import sys

n, m = map(int, sys.stdin.readline().split(' '))
dict = {}

for i in range(n):
    dict[str(i+1)] = []

for i in range(n):
    pocket = sys.stdin.readline().rstrip()
    dict[str(i+1)] = pocket

bb = {v:k for k, v in dict.items()} # 시간복잡도 O(n)

for j in range(m):
    wonder = sys.stdin.readline().rstrip()
    if wonder in dict:
        print(dict[wonder]) # 시간복잡도 O(1)
    else:
        print(bb[wonder]) # 시간복잡도 O(1)



