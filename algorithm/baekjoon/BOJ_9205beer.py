from collections import deque

def bfs():
    q = deque()
    q.append((hx, hy))
    while q:
        x, y = q.popleft()
        if abs(x-fx) + abs(y-fy) <= 50*20:
            return print('happy')
        for c in range(n):
            if visited[c] == False:
                nx = con[c][0]
                ny = con[c][1]
                if abs(x-nx) + abs(y-ny) <= 50*20:
                    visited[c] = True
                    q.append((nx, ny))
    return print('sad')



t = int(input())
for tc in range(1, t+1):
    n = int(input())
    hx, hy = map(int, input().split()) # 집
    con = [] # 편의점
    for _ in range(n):
        cx, cy = map(int, input().split())
        con.append([cx, cy])
    fx, fy = map(int, input().split()) # 락페
    visited = [False] * n
    # print(hx, hy)
    # print(c)
    # print(fx, fy)
    bfs()