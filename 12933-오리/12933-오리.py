import sys
from collections import deque

word = list(map(str, sys.stdin.readline().rstrip()))

duck = deque(['q', 'u', 'a', 'c', 'k'])

count = 0

def imple(words):
    test = []
    for i in range(len(words)):
        if len(duck) > 0:
            if words[i] == duck[0]:
                if len(duck) == 1:
                    duck.popleft()
                    words[i] = "end"
                elif len(duck) == 5:
                    duck.popleft()
                    words[i] = "first"
                else:
                    test.append(i)
                    duck.popleft()
            if len(duck) == 0:
                for j in test:
                    words[j] = count
    return words

for i in word:
    if i == 'q':
        imple(word)
        count += 1
        duck = deque(['q', 'u', 'a', 'c', 'k'])

wrong = 0 # 이상할때 -1로 바뀜

f_c = 0

final = []
for i in word:
        final.append(i)

c2 = 0

for i in final:
    if i == 'end':
        c2 += 1
    if i == "first":
        f_c += 1

if ('q' in final) or ('u' in final) or ('a' in final) or ('c' in final) or ('k' in final):
    wrong = -1
cc = 0
def ha(wor):
    w = ['end', 'first']

    for i in range(len(wor)):
        if len(w) > 0:
            if wor[i] == w[len(w)-1]:
                w.pop()
                wor[i] = 'not'
                if len(w) == 0:
                    w = ['end', 'first']

for i in final:
    if i == "first" and c2 > 0 and f_c > 0:
        c2 -= 1
        f_c -= 1
        ha(final)
        cc += 1


if len(word) % 5 != 0 or wrong == -1 or cc == 0:
    print(-1)
else:
    print(cc)



