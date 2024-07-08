from collections import deque

data1 = deque(map(int, input().rstrip()))
data2 = deque(map(int, input().rstrip()))
data3 = deque(map(int, input().rstrip()))
data4 = deque(map(int, input().rstrip()))

test = int(input())

dir = [data1, data2, data3, data4]

def rotate_1(r):
    global data, dir
    for i in range(r, 3):
        if dir[i][2] != dir[i+1][6]:
            data[i+1] = data[i] * -1
        else:
            break

def rotate_2(r):
    global data, dir
    for i in range(r, 0, -1):
        if dir[i][6] != dir[i - 1][2]:
            data[i - 1] = data[i] * -1
        else:
            break

# test 만큼 톱니바퀴 회전
for i in range(test):
    num, direct = map(int, input().split())
    # 어느 방향으로 회전할 것인지
    data = [0, 0, 0, 0]
    if num == 1:
        data[0] = direct
        rotate_1(0)
    elif num == 2:
        data[1] = direct
        if dir[1][6] != dir[0][2]:
            data[0] = data[1] * -1
        rotate_1(num-1)
    elif num == 3:
        data[2] = direct
        rotate_2(num-1)
        if dir[2][2] != dir[3][6]:
            data[3] = data[2] * -1
    elif num == 4:
        data[3] = direct
        rotate_2(num-1)
    # 회전
    for j in range(len(data)):
        if data[j] != 0:
            dir[j].rotate(data[j])

count = 0
grade = 1
for k in range(len(dir)):
    if dir[k][0] == 0:
        pass
    elif dir[k][0] == 1:
        count += grade
    grade *= 2

print(count)


