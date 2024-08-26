import sys

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split(' ')))
global count
count = 0
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in data:
    if i == 1:
        pass
    elif is_prime_number(i) is True:
        count += 1

print(count)
