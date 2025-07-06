from collections import deque

N, W, L = map(int, input().split())

queue = deque()

data = deque(list(map(int, input().split())))

time = 0
total_w = 0

for _ in range(W):
    queue.append(0)

while queue:
    time += 1
    total_w -= queue.popleft()
    if len(data) > 0:
        if total_w + data[0] <= L:
            truck = data.popleft()
            queue.append(truck)
            total_w += truck
        else:
            queue.append(0)
    if not data and total_w == 0:
        break

print(time)
