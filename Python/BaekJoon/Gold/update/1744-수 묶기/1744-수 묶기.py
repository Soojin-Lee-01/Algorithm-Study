"""
시간복잡도를 생각해보자.
O(n) : data를 담는다.
O(n log n) : 정렬한다.

총 : O(n log n)
"""
from collections import deque

####### data에 담는다. #######
n = int(input())
data = []
for _ in range(n):
    num = int(input())
    data.append(num)

answer = 0

max_num = deque()
zero = deque()
min_num = deque()

for i in range(len(data)):
    if data[i] > 0:
        max_num.append(data[i])
    elif data[i] < 0:
        min_num.append(data[i])
    else:
        zero.append(data[i])

####### 양수 값 처리한다. #######
max_num = deque(sorted(max_num, reverse=True))
temp = len(max_num) // 2
if len(max_num) >= 2:
    for j in range(temp):
        if max_num[0] != 1 and max_num[1] != 1:
            answer += (max_num.popleft() * max_num.popleft())
        elif max_num[0] == 1:
            break

for j in range(len(max_num)):
    answer += max_num[j]

####### 음수 값 처리한다. ######
min_num = deque(sorted(min_num))
temp = len(min_num) // 2
if (len(min_num)) >= 2:
    for j in range(temp):
        answer += (min_num.popleft() * min_num.popleft())

if len(zero) > 0:
    pass
else:
    for k in range(len(min_num)):
        answer += min_num[k]

print(answer)
