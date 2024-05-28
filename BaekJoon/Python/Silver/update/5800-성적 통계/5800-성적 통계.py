from collections import deque

test = int(input())

for i in range(test):
    data = deque(list(map(int, input().split(' '))))
    number = data.popleft()
    max_grade = max(data)
    min_grade = min(data)
    gaps = 0
    data = sorted(data, reverse=True)
    for j in range(len(data)-1):
        if data[j] - data[j+1] > gaps:
            gaps = data[j] - data[j+1]
    print("Class " + str(i+1))
    print("Max " + str(max_grade) + ", " + "Min " + str(min_grade) + ", " + "Largest gap " + str(gaps))