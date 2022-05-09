from collections import deque

def start(N, M, iceberg):
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] != 0:
                return i, j
    return -1, -1

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    while q:
        i, j = q.popleft()
        visited[i][j] = True
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if iceberg[ni][nj] != 0 and visited[ni][nj] == False:
                    visited[ni][nj] = True
                    q.append((ni, nj))
                elif iceberg[ni][nj] == 0 and visited[ni][nj] == True:
                    pass
                elif iceberg[ni][nj] == 0 and iceberg[i][j] > 0:
                    iceberg[i][j] -= 1
    return iceberg

def ice_cnt(ui, uj):
    # global cnt
    q = deque()
    q.append((ui, uj))
    cnt_vs[ui][uj] = True

    while q:
        i, j = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if iceberg[ni][nj] !=0 and cnt_vs[ni][nj] == False:
                    cnt_vs[ni][nj] = True
                    q.append((ni, nj))

    for i in range(N):
        for j in range(M):
            if iceberg[i][j] != 0 and cnt_vs[i][j] == False:
                return False
    return True

# bfs로 검색하면서 동,서,남,북 얼음이 있으면 -1 해주고 (0 까지만) => 1년동안 빙산이 녹음
# 하나 방문 하면 그 다음 정점 가기 전에 visited 다시 초기화
# 빙산이 처음 0대로 녹아야됨... 중간에 녹아 사라지는 빙산들의 영향은 ㄴㄴ

# bfs 한 번 돌려서 1년치 빙산 녹임 -> 그 다음에 visited 초기화
# 빙산 갯수(ice_cnt) 카운트해서 2개 이상이면, 걸린 시간(time)(bfs 돌린 횟수) 카운트한 것 최종 출력

N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
# print(iceberg)
# print(visited)
time = 0

while True:
    time += 1
    cnt = 1
    visited = [[False] * M for _ in range(N)]
    cnt_vs = [[False] * M for _ in range(N)]
    si, sj = start(N, M, iceberg)
    iceberg = bfs(si, sj)

    # for i in range(N):
    #     for j in range(M):
    #         if iceberg[i][j] != 0 and visited[i][j] == False:
    ui, uj = start(N, M, iceberg)
    ice_cnt(ui, uj)
    # for i in range(N):
    #     for j in range(M):
    #         if iceberg[i][j] !=0 and cnt_vs[i][j] == False:
    #             cnt += 1
    # if cnt >= 2:
    #     print(time)
    #     break
    # elif cnt == 0:
    #     print(0)
    #     break
    if ice_cnt(ui, uj)==False:
        print(time)
        break
    elif ui == -1 and uj == -1:
        print(0)
        break
# time = 0
# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if iceberg[i][j] != 0 and visited[i][j] == False:
#             bfs(i, j)
#             time += 1
#             visited[i][j] = False
#             ice_cnt(i, j)
#             cnt += 1
# print(time, cnt)