import sys
from collections import deque

test = int(sys.stdin.readline())

for j in range(test):
    N, M = map(int, sys.stdin.readline().split())
    word = list(map(int, sys.stdin.readline().split()))
    for i in range(len(word)):
        word[i] = [word[i], i]
    queue = deque(word)
    if N == 1:
        print("1")
    elif N > 1:
        target = M
        count = 0
        max = 0
        while queue:
            for k in queue:
                if k[0] > max:
                    max = k[0]
            if queue[0][0] < max:
                queue.rotate(-1)
            elif queue[0][0] == max:
                a = queue.popleft()
                max = 0
                count += 1
                if a[1] == target:
                    print(count)
                    break











