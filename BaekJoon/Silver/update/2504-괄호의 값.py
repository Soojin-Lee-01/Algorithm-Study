import sys

# 입력 문자열을 리스트로 변환하여 저장
data = list(sys.stdin.readline().rstrip())

# 괄호 저장 스택
stack = []

# 결과값과 가중치
result = 0
res = 1

for i in range(len(data)):
    # 여는 괄호일 경우
    if data[i] == '(':
        # 가중치에 2를 곱한다.
        res *= 2
        stack.append(data[i])

    elif data[i] == '[':
        # 가중치에 3을 곱한다.
        res *= 3
        stack.append(data[i])

    # 닫는 괄호인 경우
    elif data[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
            # 결과 값에 더해주고 2로 나눈다.
        if data[i - 1] == '(': result += res
        res //= 2
        stack.pop()

    elif data[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
            # 결과 값에 더해주고 3로 나눈다.
        if data[i - 1] == '[': result += res
        res //= 3
        stack.pop()

if len(stack) != 0:
    print(0)
else:
    print(result)