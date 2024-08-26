from collections import deque

test = int(input())

for i in range(test):
    data = deque(list(map(int, input().split())))
    data.popleft()
    num_max = max(data)
    num_min = min(data)
    data = sorted(data, reverse=True)
    num_gaps = 0
    for j in range(len(data)-1):
        if data[j] - data[j+1] > num_gaps:
            num_gaps = data[j] - data[j+1]
    print("Class " + str(i+1))
    print("Max " + str(num_max) + ", " + "Min " + str(num_min) + ", " + "Largest gap " + str(num_gaps))
