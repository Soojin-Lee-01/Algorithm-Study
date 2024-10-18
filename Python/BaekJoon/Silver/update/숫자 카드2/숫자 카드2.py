N = int(input())
data = list(map(int, input().split()))

M = int(input())
answer = list(map(int, input().split()))

dic = {}

for n in data:
    if n not in dic:
        dic[n] = 1
    elif n in dic:
        dic[n] += 1

final = []

for n in dic.keys():
    final.append(n)

final.sort()

def solution(num):
    left = 0
    right = len(final) -1

    while left <= right:
        mid = (left + right) // 2
        if (final[mid]) == num:
            return 1
        elif final[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return 0

result = [0 for _ in range(len(answer))]

for i in range(len(answer)):
    temp = solution(answer[i])
    if temp == 1:
        result[i] = dic[answer[i]]

print(' '.join(map(str, result)))
