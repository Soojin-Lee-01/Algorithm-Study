import sys

num = int(sys.stdin.readline())

file = {}

for i in range(num):
    name = sys.stdin.readline().rstrip().split('.')[1]
    if name in file:
        file[name] += 1
    else:
        file[name] = 1

organi_file = sorted(file.items()) # 딕셔너리의 키, 값 쌍 얻기

for key, value in organi_file:
    print(key, value)



