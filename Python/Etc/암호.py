num = int(input())
word = input()
n = len(word) // num

data = []
temp = ''

word = word.replace('#','1')
word = word.replace('*', '0')

for i in range(0, len(word)-1, len(word)//num):
    data.append(word[i:i+len(word)//num])

result = []
for binary_str in data:
    result.append(int(binary_str, 2))

final = []
for n in result:
    final.append(chr(n))

print(''.join(final))
