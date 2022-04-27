from collections import deque

def BFS():
    # cnt = 0
    while q:
        ci, cj = q.popleft()
        # for i in range(N*H):
        #     for j in range(M):
        # if tmt[ci][cj] != 0:
        #     return tmt[ci][cj] -1
        for k in range(6):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0<=ni<N*H and 0<=nj<M and tmt[ci][cj] != -1 and tmt[ni][nj] == 0:
                if k < 4:
                    q.append((ni, nj))
                    tmt[ni][nj] = tmt[ci][cj] + 1
                # -1인경우 N으로 나눴을 때 N-1이면 층이 바뀌는거니까 안됨
                elif k == 4:
                    if ni % N != N - 1:
                        q.append((ni, nj))
                        tmt[ni][nj] = tmt[ci][cj] + 1
                    # +1인경우 N으로 나눌 때 0이면 층이 바뀌니까 안됨
                elif k == 5:
                    if ni % N != 0:
                        q.append((ni, nj))
                        tmt[ni][nj] = tmt[ci][cj] + 1

    # return cnt
            # if tmt[i][j] == 1:
            #     if 0<=i-N<N*H and 0<=i+N<N*H and tmt[i-N][j] == -1 and tmt[i+N][j] == 0:
            #         tmt[i - N][j] = 1
            #         tmt[i + N][j] = 1
            #     elif 0<=i-N<N*H and tmt[i-N][j] == 0:
            #         tmt[i - N][j] = 1
            #     elif 0<=i+N<N*H and tmt[i+N][j] == 0:
            #         tmt[i + N][j] = 1



# 상자 크기 가로 M, 세로 N, 높이 H
M, N, H = map(int, input().split())
tmt = [list(map(int, input().split())) for _ in range(N*H)]

q = deque()
di = [0, 0, -N, N, -1, 1]
dj = [1, -1, 0, 0, 0, 0]

for i in range(N*H):
    for j in range(M):
        if tmt[i][j] == 1:
            q.append((i, j))

BFS()
sol = 0
x = 0
maxV = 0
for t in tmt:
    for a in t:
        if a == 0:
            print(-1)
            exit(0)
        else:
            if maxV <= a:
                maxV = a
                sol = maxV -1
# if x == -1:
#     print(x)
# else:
print(sol)

