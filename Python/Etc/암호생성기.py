from collections import deque
 
def solution(da):
    count = 1
    while True:
        for _ in range(8):
            number = da.popleft()
            number -= count
            da.append(number)
            count += 1
            if count == 6:
                count = 1
            if da[7] <= 0:
                da[7] = 0
                return da
 
for _ in range(10):
    t = int(input())
    data = list(map(int, input().split()))
    data = deque(data)
 
    print(f'#{t}', ' '.join(map(str, solution(data))))
