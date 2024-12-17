"""
Union-Find 알고리즘
분리 집합을 트리로 표현

- 원소들이 어떤 그룹에 속해 있는지 파악
- 두 그룹 합치거나, 특정 그룹을 찾는 등 연산 수행할 때 사용
Union, Find
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    cal, a, b = map(int, input().split())

    if cal == 0:
        union_parent(a, b)
    else:
        if find_parent(a) != find_parent(b): print("NO")
        else: print("YES")
