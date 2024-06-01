from collections import deque

test = int(input())

for i in range(test):
    word = input()
    num = int(input())
    # 양쪽 사이드 제거
    data = deque(input()[1:-1].split(','))

    # 에러 체크 위한 것
    check = 1

    # 만약에 0이라면 큐에 아무것도 없음
    if num == 0:
        data = deque()
    # 뒤집기 횟수
    rev = 0

    for j in range(len(word)):
        # 뒤집기 일때 더하기
        if word[j] == 'R':
            rev += 1
        # 삭제하기 일때 확인
        elif word[j] == 'D':
            # 만약에 데이터가 비어있으면 에러 체크
            if len(data) == 0:
                print("error")
                # 에러였다고 표시
                check = 0
                break
            # 만약에 데이터가 비어있지 않으면
            else:
                # 만약에 뒤집기가 짝수이면 앞에서 삭제
                if rev % 2 == 0:
                    data.popleft()
                # 만약에 홀수이면 뒤에서 삭제
                else:
                    data.pop()

    if check == 0:
        continue
    else:
        # 만약에 뒤집기가 짝수이면 그대로 출력
        if rev % 2 == 0:
            print('[' + ','.join(data) + ']')
        # 뒤집기가 홀수이면 뒤집고 출력
        else:
            data.reverse()
            print('[' + ','.join(data) + ']')