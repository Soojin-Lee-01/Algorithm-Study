import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for i in range(N):
    word = sys.stdin.readline().split()
    if word[0] == "push":
        queue.append(word[1])
    elif word[0] == "pop":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print("-1")
    elif word[0] == "size":
        print(len(queue))
    elif word[0] == "empty":
        if len(queue) > 0:
            print("0")
        else:
            print("1")
    elif word[0] == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print("-1")
    else:
        if len(queue) > 0:
            print(queue[len(queue)-1])
        else:
            print("-1")

