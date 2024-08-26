import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
result = []
def is_prime_number(x):
    for i in range(2, x):
        if x % i != 0:
            pass
        else:
            return False
    return True

for k in range(M, N+1):
    if k == 1:
        pass
    else:
        if is_prime_number(k) is True:
            result.append(k)

sum = 0

if len(result) > 0:
    for i in result:
        sum += i
    print(sum)
    print(min(result))
else:
    print("-1")

