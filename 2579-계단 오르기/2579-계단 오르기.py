import sys

num = int(sys.stdin.readline())
game = [0] * 301
for i in range(num):
    a = int(sys.stdin.readline().rstrip())
    game[i+1] = a

mem = [0] * 301
mem[1] = game[1]
mem[2] = game[1] + game[2]
mem[3] = max((game[2] + game[3]), (game[1] + game[3]))

for i in range(4, num+1):
    mem[i] = max((game[i] + mem[i-2]) , (game[i] + game[i-1] + mem[i-3]))

print(mem[num])
