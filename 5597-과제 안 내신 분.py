test= []

for i in range(30):
    test.append(i+1)

for i in range(28):
    a = int(input())
    test.remove(a)

print(min(test))
print(max(test))