num = int(input())

# 기둥
data = [0 for _ in range(1001)]

max_index = 0
max_he = 0

# 가장 높은 높이와 인덱스 찾기
for i in range(num):
    a, b = map(int, input().split())
    data[a] = b
    if max_he < b:
        max_he = b
        max_index = a

water = 0
temp = 0
# 왼쪽에서 가장 큰 기둥 만큼 더하기
for i in range(max_index):
    temp = max(temp, data[i])
    water += temp


temp = 0
# 오른쪽에서 가장 큰 기둥 만큼 더하기
for i in range(len(data)-1, max_index-1, -1):
    temp = max(temp, data[i])
    water += temp

print(water)
