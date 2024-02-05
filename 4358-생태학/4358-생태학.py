import sys

tree_dict = {}

count = 0

while True:
    word = sys.stdin.readline().rstrip()
    if word == '':
        break
    count += 1
    if word in tree_dict:
        tree_dict[word] += 1
    else:
        tree_dict[word] = 1

sort_list = dict(sorted(tree_dict.items()))

for key, value in sort_list.items():
    percent = (value / count * 100)
    print("%s %.4f" % (key, percent))

"""
<round>가 안되는 이유
- round(0.5) = 0 , round(1.5) = 2
float에 대한 round()의 동작은 예상과 다를 수 있습니다: 
예를 들어, round(2.675, 2)는 2.68 대신에 2.67을 제공합니다. 
이것은 버그가 아닙니다: 대부분의 십진 소수가 float로 정확히 표현될 수 없다는 사실로부터 오는 결과입니다.
"""
