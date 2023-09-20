from collections import deque
import sys

q= deque()

n = int(sys.stdin.readline())

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "push":
        q.append(a[1])
    elif a[0] == "pop":
        if(len(q) > 0):
            print(q.popleft())
        else:
            print("-1")
    elif a[0] == "front":
        if (len(q) > 0):
            print(q[0])
        else:
            print("-1")
    elif a[0] == "back":
        if(len(q) > 0):
            print(q[len(q)-1])
        else:
            print("-1")
    elif a[0] == "size":
        print(len(q))
    elif a[0] == "empty":
        if(len(q) == 0):
            print("1")
        else:
            print("0")