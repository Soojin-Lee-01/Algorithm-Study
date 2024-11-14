from collections import deque

test = int(input())

for t in range(test):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()
    data = deque(data)
    time = 0
    make = 0
    answer = "Possible"

    while data:
        # 오픈하고 바로 온 손님을 생각해야 한다.
        while data and data[0] == time:
            if make > 0:
                make -= 1
                data.popleft()
            else:
                answer = "Impossible"
                break

        if answer == "Impossible":
            break

        time += 1
        if time % M == 0:
            make += K

    print(f'#{t+1} {answer}')
