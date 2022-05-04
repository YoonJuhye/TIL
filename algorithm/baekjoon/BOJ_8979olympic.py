

N, K = map(int, input().split()) # 국가 수, 지정국가
nat = [list(map(int, input().split())) for _ in range(N)]


nat_gold = [0]*(N+1)
nat_silver = [0]*(N+1)
nat_bronze = [0]*(N+1)
for i in range(N):
    nat_gold[nat[i][0]] = nat[i][1]
    nat_silver[nat[i][0]] = nat[i][2]
    nat_bronze[nat[i][0]] = nat[i][3]
# print(nat_gold)
# print(nat_silver)
# print(nat_bronze)
cnt = 1
for j in range(N+1):
    if j != K:
        if nat_gold[j] > nat_gold[K]:
            cnt += 1
        elif nat_gold[j] == nat_gold[K]:
            if nat_silver[j] > nat_silver[K]:
                cnt += 1
            elif nat_silver[j] == nat_silver[K]:
                if nat_bronze[j] > nat_bronze[K]:
                    cnt += 1
print(cnt)


# print(nat)
# score = [0]*(N+2)
# for i in range(1, N):
#     if nat[i-1][1] < nat[i][1]: # 금메달 개수
#        score[i] = nat[i][0]
#     elif nat[i-1][1] == nat[i][1]:
#         if nat[i-1][2] < nat[i][2]: # 은메달 개수
#             score[i] = nat[i][0]
#         elif nat[i-1][2] == nat[i][2]:
#             if nat[i-1][3] < nat[i][3]: # 동메달 개수
#                 score[i] = nat[i][0]
#             elif nat[i-1][3] > nat[i][3]:
#                 score[i] = nat[i-1][0]
#         elif nat[i-1][2] > nat[i][2]:
#             score[i] = nat[i-1][0]
#     elif nat[i-1][1] > nat[i][1]:
#         score[i] = nat[i-1][0]
#
# result = score.index(K)
# print(result)
