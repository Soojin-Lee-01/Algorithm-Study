# 밑변과 높이를 받음
n, m = map(int, input().split(' '))

# 물이 채워진 정도를 받음
water = list(map(int, input().split(' ')))

# 물이 얼마나 채워졌는지
result = 0

for i in range(1, m-1):
    left = max(water[:i])
    right = max(water[i+1:])

    com = min(left, right)

    if com > water[i]:
        result += (com - water[i])

print(result)