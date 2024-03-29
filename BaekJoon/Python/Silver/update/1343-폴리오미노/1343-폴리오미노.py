import sys

# Solution-1
word = sys.stdin.readline().rstrip()

data = []
num = ''
num2 = ''
for i in range(len(word)):
    if word[i] != '.':
        if len(num2) > 0 :
            data.append(num2)
            num2 = ''
        num += word[i]
    else:
        if len(num) > 0 :
            data.append(num)
            num = ''
        num2 += word[i]

if len(num) > 0:
    data.append(num)
elif len(num2) > 0:
    data.append(num2)

for i in range(len(data)):
    if data[i][0] == '.':
        pass
    else:
        if len(data[i]) % 2 == 1:
            print(-1)
            exit()
        else:
            if len(data[i]) % 4 == 0:
                a = ''
                a += len(data[i]) * 'A'
                data[i] = a
            else:
                a = ''
                a += ((len(data[i]) // 4) * 4) * 'A'
                a += (len(data[i]) - ((len(data[i]) // 4) * 4)) * 'B'
                data[i] = a

print(''.join(data))


# Solution -2

board = sys.stdin.readline().rstrip()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)