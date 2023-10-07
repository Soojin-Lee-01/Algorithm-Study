import sys
from  collections import deque

n = int(sys.stdin.readline())
data = deque() # 입력을 받음
stack = [] # 입려과 같은 순서로 숫자를 담을 리스트

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    data.append(a)

result = deque() # 담을 오름차순 숫자들

for i in range(n):
    result.append(i+1)

no = [] # 연산자 담을 리스트

while data:
    if len(stack) == 0:
        stack.append(result.popleft())
        no.append("+")
    elif stack[len(stack)-1] == data[0]:
        stack.pop()
        no.append("-")
        data.popleft()
    elif stack[len(stack)-1] < data[0]:
        stack.append(result.popleft())
        no.append("+")
    elif stack[len(stack)-1] > data[0]:
        no.append("NO")
        break

if "NO" in no:
    print("NO")
else:
    for i in no:
        print(i)





