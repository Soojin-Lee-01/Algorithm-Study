data1 = list(input())
data2 = list(input())

while len(data1) != len(data2):
    # 만약에 맨 뒤가 A라면 제거
    if data2[-1] == 'A':
        data2.pop()
    # 만약에 맨 뒤가 B라면 제거 후 뒤집기
    elif data2[-1] == 'B':
        data2.pop()
        data2.reverse()
    # 만약에 data1과 data2가 같다면 종료
    if data1 == data2:
        print(1)
        exit()

# 같지 않다면 0 출력
print(0)