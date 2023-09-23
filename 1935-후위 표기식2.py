import sys
n = int(sys.stdin.readline()) # 문자열을 정수로 변환하면서 \n자동으로 제거
word = sys.stdin.readline().rstrip() # \n 제거 해줘야함
num = [0]*n
for i in range(n):
    num[i] = int(sys.stdin.readline())
stack = []
for i in word:
    if 'A' <= i <= 'Z':
        stack.append(num[ord(i) - ord('A')]) #해당 문자의 유니코드 값을 반환
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)
print('%.2f' % stack[0])