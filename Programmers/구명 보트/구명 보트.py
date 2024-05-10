from collections import deque

def solution(people, limit):
    people = sorted(people, reverse=True)
    per = deque(people)
    count = 0
    weight = limit
    while len(per) > 1:
        if weight >= per[0] + per[-1]:
            per.popleft()
            per.pop()
            count += 1
        else:
            count += 1
            per.popleft()

    if per:
        count += 1
    return count