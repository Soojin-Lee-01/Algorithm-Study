import sys

h, m = map(int,sys.stdin.readline().split(' '))
time = int(sys.stdin.readline())

if m + time >= 60:
    h += (m + time) // 60
    m = (m+time) % 60
else:
    m = m + time

if h >= 24:
    h -= 24

print(h, m)


