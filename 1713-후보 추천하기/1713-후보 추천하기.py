import sys
from collections import deque

n = int(sys.stdin.readline())
num = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().rstrip().split(' ')))


score = {}
for i in range(100):
    score[i+1] = 0

photo = deque()
re = []
if num > 0:
    for i in data:
        if i not in photo:
            if len(photo) < n:
                photo.append(i)
                score[i] += 1
            else:
                min_score = 10000
                for j in photo:
                    if score[j] < min_score:
                        min_score = score[j]
                count = 0
                for k in photo:
                    if score[k] == min_score:
                        count += 1
                        re.append(k)
                if len(re) == n:
                    a = photo.popleft()
                    score[a] = 0
                    re.clear()
                    min_score = 10000
                elif len(re) > 1:
                    photo.remove(re[0])
                    score[re[0]] = 0
                    re.clear()
                    min_score = 10000
                elif len(re) == 1:
                    if len(photo) > 0:
                        photo.remove(re[0])
                        score[re[0]] = 0
                        re.clear()
                        min_score = 10000
                photo.append(i)
                score[i] += 1

        else:
            score[i] += 1
    photo = list(photo)
    photo.sort()
    print(' '.join(map(str, photo)))

else:
    print(0)
