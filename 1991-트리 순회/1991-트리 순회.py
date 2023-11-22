import sys

N = int(sys.stdin.readline())

graph = {}

for i in range(N):
    graph[chr(65+i)] = []

for i in range(N):
    a, b, c = map(str, sys.stdin.readline().split())
    graph[a].append(b)
    graph[a].append(c)

# 전위 순회
def preorder(str):
    if str == '.':
        return
    print(str, end='')
    preorder(graph[str][0])
    preorder(graph[str][1])

# 중위 순회
def inorder(str):
    if str == '.':
        return
    inorder(graph[str][0])
    print(str, end='')
    inorder(graph[str][1])

# 후위 순회
def postorder(str):
    if str == '.':
        return
    postorder(graph[str][0])
    postorder(graph[str][1])
    print(str, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')