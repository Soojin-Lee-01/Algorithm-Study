N, M = map(int, input().split())
data = list(map(int, input().split()))

def solution(num):
    global temp
    left = 0
    right = max(data)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        te = 0
        for i in data:
            if mid < i:
                te += (i - mid)
        if te > num:
            answer = max(answer, mid)
            left = mid + 1
        elif te < num:
            right = mid - 1

        else:
            answer = max(answer, mid)
            right = mid - 1

    return answer

print(solution(M))
