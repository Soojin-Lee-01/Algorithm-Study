n, m = map(int, input().split())
data = list(map(int, input().split()))
result = []

def permu(n, combo = []):
    if len(combo) == n:
        result.append(combo[:])
        return
    for element in data:
        combo.append(element)
        permu(n, combo)
        combo.pop()

permu(m)

result = sorted(result)

for i in range(len(result)):
    print(' '.join(map(str, result[i])))
