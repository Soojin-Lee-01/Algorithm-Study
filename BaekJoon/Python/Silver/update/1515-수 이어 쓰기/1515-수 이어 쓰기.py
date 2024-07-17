from collections import deque

num = deque(input().rstrip())

count = 1

while True:
    if len(num) == 0:
        break
    if str(count) == num[0]:
        num.popleft()
    else:
        temp = str(count)
        for j in range(len(temp)):
            if len(num) > 0:
                if temp[j] == num[0]:
                    num.popleft()
            else:
                break

    count += 1

print(count-1)
