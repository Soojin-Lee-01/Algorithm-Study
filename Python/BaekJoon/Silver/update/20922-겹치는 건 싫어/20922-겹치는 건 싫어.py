N, K = map(int, input().split())
data = list(map(int, input().split()))

left = 0
count_map = {}
max_length = 0

for right in range(N):
    if data[right] in count_map:
        count_map[data[right]] += 1
    else:
        count_map[data[right]] = 1

    while count_map[data[right]] > K:
        count_map[data[left]] -= 1
        if count_map[data[left]] == 0:
            del count_map[data[left]]
        left += 1

    max_length = max(max_length, right - left + 1)

print(max_length)
