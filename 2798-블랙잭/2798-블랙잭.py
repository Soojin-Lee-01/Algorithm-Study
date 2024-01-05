import sys

n, m = map(int, sys.stdin.readline().split(' '))

word = list(map(int, sys.stdin.readline().rstrip().split(' ')))

num = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = word[i] + word[j] + word[k]

            if sum > m:
                continue
            else:
                num.append(sum)

print(max(num))