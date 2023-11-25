import sys

result = []

for i in range(30):
    result.append(i+1)

for i in range(28):
    score = int(sys.stdin.readline())
    result.remove(score)

print(min(result))
print(max(result))