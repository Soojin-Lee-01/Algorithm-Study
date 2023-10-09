import sys

k = int(sys.stdin.readline())

n = list(map(int, sys.stdin.readline().rstrip().split()))

result = [[] for _ in range(k)]

def Tree(first, last, k):
    if first == last:
        result[k].append(n[first])
        return
    mid = (first + last) // 2
    result[k].append(n[mid])
    Tree(first, mid-1, k+1)
    Tree(mid+1, last, k+1)

Tree(0, len(n)-1, 0)

for i in range(k):
    for j in result[i]:
        print(j, end=' ')
    print()

"""
<반복 - 재귀>
n의 가운데가 root 노드
가운데를 기준으로 왼쪽 노드와 오른쪽 노드를 나누어서 다시 가운데가 root 노드
"""