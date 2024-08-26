N, M, P, C, D = map(int, input().split(' '))
x, y = map(int, input().split(' ')) # 루돌프의 좌표
deer = [x-1, y-1] # 루돌프의 좌표 저장
board = [[0 for _ in range(N)] for _ in range(N)] # 루돌프, 산타 위치 그래프
board[x-1][y-1] = -1 # 루돌프면 -1
santas = [[0, 0] for _ in range(P)] # 산타의 좌표 저장
score = [0] * P # 산타들의 점수
down = [0] * P # 기절한 산타
dead = [False] * P # 탈락한 산타

ddx=[-1,-1,0,1,1,1,0,-1]
ddy=[0,1,1,1,0,-1,-1,-1]
sdx=[-1,0,1,0]
sdy=[0,1,0,-1]

for _ in range(P):
    num, r, c = map(int, input().split(' '))
    santas[num-1] = [r-1, c-1]
    board[r-1][c-1] = num

def distance(x,y,r,c):
    return (x-r)*(x-r)+(y-c)*(y-c)

def move_deer():
    global deer,dead
    x,y=deer
    board[x][y]=0
    candidates=[]
    for i in range(P):
        if not dead[i]:
            r,c=santas[i]
            dis=distance(x,y,r,c)
            candidates.append((dis,r,c))
    candidates.sort(key=lambda x:(x[0],-x[1],-x[2]))
    tx,ty=candidates[0][1],candidates[0][2] #find target santa

    candidates=[]
    for i in range(8):
        nx,ny=x+ddx[i],y+ddy[i]
        if 0<=nx<N and 0<=ny<N:
            dis=distance(nx,ny,tx,ty)
            candidates.append((dis,nx,ny,i))
    candidates.sort()
    nx,ny,dir=candidates[0][1],candidates[0][2],candidates[0][3]
    deer=[nx,ny]
    if board[nx][ny]:
        crash(board[nx][ny],0,dir)
    board[nx][ny]=-1


def move_santas():
    global dead, down, deer, santas
    x, y = deer
    for i in range(P):
        if not dead[i] and (down[i] == 0):
            candidates = []
            r, c = santas[i]
            original_dis = distance(x, y, r, c)
            for d in range(4):
                nr, nc = r + sdx[d], c + sdy[d]
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] <= 0:
                        dis = distance(x, y, nr, nc)
                        if dis < original_dis:
                            candidates.append((dis, d))  # move santa who is not dead or down

            if candidates:
                candidates.sort()
                dir = candidates[0][1]
                nr, nc = r + sdx[dir], c + sdy[dir]
                santas[i] = [nr, nc]
                if board[nr][nc] == -1:
                    board[r][c] = 0
                    crash(i + 1, 1, (dir + 2) % 4)
                else:
                    board[nr][nc] = board[r][c]
                    board[r][c] = 0


def crash(santa_num, case, dir):
    global santas, score, dead, down
    idx = santa_num - 1
    r, c = santas[idx]
    if case == 0:
        nr, nc = r + ddx[dir] * C, c + ddy[dir] * C
        if 0 <= nr < N and 0 <= nc < N:
            santas[idx] = [nr, nc]
            down[idx] = 2
            if not board[nr][nc]:
                board[nr][nc] = santa_num
            else:
                interact(santa_num, board[nr][nc], 0, dir)
        else:
            dead[idx] = True
        score[idx] += C
    else:
        nr, nc = r + sdx[dir] * D, c + sdy[dir] * D
        if 0 <= nr < N and 0 <= nc < N:
            santas[idx] = [nr, nc]
            down[idx] = 2
            if not board[nr][nc]:
                board[nr][nc] = santa_num
            else:
                interact(santa_num, board[nr][nc], 1, dir)
        else:
            dead[idx] = True
        score[idx] += D


def interact(incoming,stable,case,dir):
    global board,santas
    idx1,idx2=incoming-1,stable-1
    r1,c1=santas[idx1]
    r2,c2=santas[idx2]
    if case==0:
        nr2,nc2=r2+ddx[dir],c2+ddy[dir]
        if 0<=nr2<N and 0<=nc2<N:
            santas[idx2]=[nr2,nc2]
            if not board[nr2][nc2]:
                board[nr2][nc2]=stable
                board[r1][c1]=incoming
            else:
                board[r1][c1]=incoming
                interact(stable,board[nr2][nc2],0,dir)
        else:
            board[r1][c1]=incoming
            dead[idx2]=True
    else:
        nr2,nc2=r2+sdx[dir],c2+sdy[dir]
        if 0<=nr2<N and 0<=nc2<N:
            santas[idx2]=[nr2,nc2]
            if not board[nr2][nc2]:
                board[nr2][nc2]=stable
                board[r1][c1]=incoming
            else:
                board[r1][c1]=incoming
                interact(stable,board[nr2][nc2],1,dir)
        else:
            board[r1][c1]=incoming
            dead[idx2]=True

def all_dead():
    global dead
    for i in range(P):
        if not dead[i]:
            return False
    return True

def go_to_next():
    global dead,down,score
    for i in range(P):
        if not dead[i]:
            score[i]+=1
            if down[i]:
                down[i]-=1


for _ in range(M):
    move_deer()
    move_santas()
    if all_dead():
        break
    go_to_next()

for i in range(P):
    print(score[i],end=' ')




