import sys

n, m, k = map(int, sys.stdin.readline().split())

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

fireballs = {}
for _ in range(m):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireballs.setdefault((r - 1, c - 1), []).append([m, s, d])

for _ in range(k):
    new_fireballs = {}
    for position, balls in fireballs.items():
        for ball in balls:
            m, s, d = ball
            dr, dc = directions[d]
            nr = (position[0] + dr * s) % n
            nc = (position[1] + dc * s) % n
            new_fireballs.setdefault((nr, nc), []).append([m, s, d])

    fireballs = new_fireballs

    for key, values in fireballs.items():

        if len(values) > 1:
            new_m = 0
            new_s = 0
            check_one = 0
            check_two = 0
            for value in values:
                new_m += value[0]
                new_s += value[1]
                if value[2] % 2 == 0:
                    check_one += 1
                else:
                    check_two += 1
            final_m = new_m //5
            final_s = new_s // len(values)
            fireballs[key] = []
            if check_one == len(values) or check_two == len(values):
                for i in range(4):
                    fireballs[key].append([final_m, final_s, 2*i])
            else:
                for j in range(1, 5):
                    fireballs[key].append([final_m, final_s, (2*j)-1])

    # 파이어볼 제거
    for key, values in fireballs.items():
        new_values = []
        for value in values:
            if value[0] != 0:
                new_values.append(value)
        fireballs[key] = new_values

result = 0
for dr, values in fireballs.items():
    for value in values:
        result += value[0]
print(result)