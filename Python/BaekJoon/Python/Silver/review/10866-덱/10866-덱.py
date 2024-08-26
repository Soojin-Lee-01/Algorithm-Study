import sys
from collections import deque

N = int(sys.stdin.readline())

deque = deque()

for i in range(N):
    word = sys.stdin.readline().split()
    if word[0] == "push_front":
        deque.append(word[1])
        deque.rotate(1)
    elif word[0] == "push_back":
        deque.append(word[1])
    elif word[0] == "pop_front":
        if len(deque) > 0:
            print(deque.popleft())
        else:
            print("-1")
    elif word[0] == "pop_back":
        if len(deque) > 0:
            print(deque.pop())
        else:
            print("-1")
    elif word[0] == "size":
        print(len(deque))
    elif word[0] == "empty":
        if len(deque) == 0:
            print("1")
        else:
            print("0")
    elif word[0] == "front":
        if len(deque) > 0:
            print(deque[0])
        else:
            print("-1")
    else:
        if len(deque) > 0:
            print(deque[len(deque)-1])
        else:
            print("-1")