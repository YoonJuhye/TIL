def ch(x, y):
    global minV
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                if brd[i+x][j+y] != 'W':
                    cnt1 += 1
                if brd[i+x][j+y] != 'B':
                    cnt2 += 1
            else:
                if brd[i+x][j+y] != 'B':
                    cnt1 += 1
                if brd[i+x][j+y] != 'W':
                    cnt2 += 1

    if minV > cnt1:
        minV = cnt1
    if minV > cnt2:
        minV = cnt2


N, M = map(int, input().split())
brd = []
for _ in range(N):
    brd.append(list(input()))

minV = 100
for i in range(0, N-7):
    for j in range(0, M-7):
        ch(i, j)
print(minV)


'''
체스판으로 안되어있는거 세기 -> 8개씩 검사..?
1. 0열 0, 2, 4, 6 행이 B 이면, 1, 3, 5, 7이 W여야 함
2. 1열 0, 2, 4, 6 행은 W 여야, 1, 3, 5, 7은 B여야 함 (반대=)
BWBWBWBWBW
WBWBWBWBWB 패턴 검색해서 틀리면...
'''

# def ch(a, b):
#     global cnt, minV
#     for i in range(8):
#         for j in range(8):
#             if i % 2 == 0: # 짝수열
#                 if j % 2 == 0 and brd[i][j] == 'B': # 짝수행이 B이면
#                     if brd[i][j+1] != 'W': # 홀수행은 W여야 함
#                         cnt += 1
#                 elif j % 2 == 0 and brd[i][j] == 'W': #짝수행이 W이면
#                     if brd[i][j+1] != 'B': # 홀수행은 B여야 함
#                         cnt += 1
#             else: # 홀수열
#                 if j % 2 == 0 and brd[i][j] == 'B':  # 짝수행이 B이면
#                     if brd[i][j + 1] != 'W':  # 홀수행은 W여야 함
#                         cnt += 1
#                 elif j % 2 == 0 and brd[i][j] == 'W':  # 짝수행이 W이면
#                     if brd[i][j + 1] != 'B':  # 홀수행은 B여야 함
#                         cnt += 1
#     return cnt



# for i in range(N):
#     cnt = 0
#     for j in range(M):
#         if brd[i][j] == 'B':
#             if brd[i][j+1] != 'W':
#                 cnt += 1
#         elif brd[i][j] == 'W':
#             if brd[i][j+1] != 'B':
#                 cnt += 1

# def bru(p, t):
#     i = 0
#     j = 0
#     cnt = 0
#     while j < M and i < N:
#         if brd[i] != p[j]:
#             i = i -j
#             j = -1
#         i = i + 1
#         j = j + 1
#     if j == M:
#         return i
#     else:
#         cnt += 1
#         return cnt

