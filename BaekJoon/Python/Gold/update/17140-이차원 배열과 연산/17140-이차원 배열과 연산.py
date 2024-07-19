r, c, k = map(int, input().split())

graph = []

# 초기 그래프 만들어줌
for i in range(3):
    data = list(map(int, input().split()))
    graph.append(data)

# 초 세기
count = 0

# 행 정렬할 때 길이만큼 0 채워주기
def sor(gr):
    n = 0
    for i in range(len(graph)):
        if len(graph[i]) > n:
            n = len(graph[i])
    for i in range(len(graph)):
        if len(graph[i]) != n:
            t = n - len(graph[i])
            for _ in range(t):
                graph[i].append(0)

    return gr

# 행 계산
def r_calc(gr):
    for k in range(len(gr)):
        temp = {}
        data = gr[k]
        for j in range(len(data)):
            if data[j] != 0:
                if data[j] not in temp:
                    temp[data[j]] = 1
                elif data[j] in temp:
                    temp[data[j]] += 1
        t_li = []
        for a, b in temp.items():
            t_li.append([a, b])
        t_li = sorted(t_li, key=lambda x: (x[1], x[0]))
        t_f = []
        for a, b in t_li:
            t_f.append(a)
            t_f.append(b)
        gr[k] = t_f
    gr = sor(gr)
    return gr

# 열 계산하고 0으로 길이만큼 채워주기
def c_calu(gr):
    t_gr = []
    max_t = 0
    for i in range(len(gr[0])):
        te = []
        for j in range(len(gr)):
            te.append(gr[j][i])
        dic = {}
        for d in te:
            if d != 0:
                if d not in dic:
                    dic[d] = 1
                elif d in dic:
                    dic[d] += 1
        t_li = []
        for a, b in dic.items():
            t_li.append([a, b])
        t_li = sorted(t_li, key=lambda x : (x[1], x[0]))
        t_f = []
        for a, b in t_li:
            t_f.append(a)
            t_f.append(b)
        t_gr.append(t_f)
        if max_t < len(t_f):
            max_t = len(t_f)
    fi_gra = [[0 for _ in range(len(t_gr))] for _ in range(max_t)]
    for k in range(len(t_gr)):
        dat = t_gr[k]
        for dd in range(len(dat)):
            fi_gra[dd][k] = dat[dd]
    return fi_gra

# 100초까지 실행, 만약 넘어가면 -1 출력
for _ in range(100):
    if len(graph) > r - 1 and len(graph[0]) > c - 1:
        if graph[r - 1][c - 1] == k:
            print(count)
            exit()
    count += 1
    # 먼저 행과 열의 갯수를 비교
    R = len(graph[0]) # 열
    C = len(graph) # 행
    if C >= R:
        graph = r_calc(graph)
    else:
        graph = c_calu(graph)
    R = len(graph[0])
    C = len(graph)
    if C > 100:
        # 중요 포인트! -> slicing 처리하자!
        graph = graph[:100]

    if R > 100:
        # 중요 포인트! -> slicing 처리하자!
        graph = [row[:100] for row in graph]

    if len(graph) > r-1 and len(graph[0]) > c-1:
        if graph[r-1][c-1] == k:
            print(count)
            exit()

print(-1)
