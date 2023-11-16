import sys
from collections import deque

N = int(sys.stdin.readline())
word = deque()
for i in range(N):
    num = int(sys.stdin.readline())
    word.append(num)

number = deque()
for i in range(N):
    number.append(i+1)
list = []
stack = []
while word:
    if len(stack) > 0 and stack[len(stack) - 1] == word[0]:
        list.append("-")
        stack.pop()
        word.popleft()
    else:
        if len(number) <= 0:
            if stack[len(stack) - 1] != word[0]:
                print("NO")
                exit()
        else:
            if number[0] != word[0]:
                stack.append(number[0])
                number.popleft()
                list.append("+")
            elif number[0] == word[0]:
                stack.append(number[0])
                number.popleft()
                list.append("+")
                stack.pop()
                list.append("-")
                word.popleft()

for i in list:
    print(i)



