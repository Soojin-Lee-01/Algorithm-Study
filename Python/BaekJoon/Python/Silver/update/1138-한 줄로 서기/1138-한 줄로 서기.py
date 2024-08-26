from collections import deque

num = int(input())

data = deque(list(map(int, input().split(' '))))

person = [0 for _ in range(num)]

count = 0

for i in range(len(data)):
    if data[i] == 0:
        for k in range(len(person)):
            if person[k] == 0:
                person[k] = i + 1
                break
    else:
        for j in range(len(person)):

            if person[j] == 0:
                ind = j
                count += 1
            if count == data[i]:
                if person[ind + 1] == 0:
                    person[ind + 1] = i + 1
                    count = 0
                    break
                else:
                    ind += 1

print(' '.join(map(str, person)))