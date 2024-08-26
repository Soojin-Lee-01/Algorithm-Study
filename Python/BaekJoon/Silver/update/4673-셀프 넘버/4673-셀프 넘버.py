def self_num(n):
    x = list(str(n))
    result = 0
    for i in range(len(x)):
        result += int(x[i])
    result = result + n
    return result

results = set()
for i in range(10000):
    results.add(self_num(i))
for m in range(1,10001):
    if m not in results:
        print(m)