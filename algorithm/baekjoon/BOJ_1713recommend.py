from collections import deque

# N : 사진틀 수 , R : 전체 추천 횟수, recNum : 추천받은 학생 번호, stuNum : 학생번호

N = int(input())
R = int(input())
recNum = list(map(int, input().split())) # 추천받은 학생 번호
# stuNum = [0]*101
cnt = [0]*101 # 추천 횟수
recPic = [] # 사진틀

# recNum을 하나씩 순회하면서 사진틀에 넣어준다
# 사진틀에 넣으면서 해당 번호의 추천 횟수를 +1 씩 해준다
# 사진틀이 N만큼 차면 추천횟수를 확인한다-> 추천횟수가 가장 낮은 값을 지운다-> 같다면, 가장 오래된 놈을 지운다.
# 만약에 이미 사진틀에 있으면 cnt만 해주고 추가하지 않음
# recNum을 모두 순회한 뒤 최종 사진틀에 있는 번호를 sort 하여 출력한다.

# for i in range(R):
# minV = 1
# picCnt = []
for i in range(R):
    if recNum[i] in recPic:
        cnt[recNum[i]] += 1
    else:
        if len(recPic) < N:
            recPic.append(recNum[i])
            cnt[recNum[i]] += 1
        elif len(recPic) >= N:
            picCnt = []
            for j in range(N):
                picCnt.append(cnt[recPic[j]])
            for k in range(N):
                if picCnt[k] == min(picCnt):
                    cnt[recPic[k]] = 0
                    del recPic[k]
                    break
            recPic.append(recNum[i])
            cnt[recNum[i]] += 1

recPic.sort()
print(*recPic)

# 추천 횟수가 가장 낮은 값을 지워야 됨
# 추천 사진틀에 있는 놈들의 추천 횟수를 리스트로 만들고, 그 리스트 중 최솟값을 구해서 지워버림

        #     if len(same)>=2:
        #         recPic.remove(recPic)
        #         break
        #     else:
        #         recPic.remove(minV)
        #         break
        # recPic.append(recNum[i])
        # cnt[recNum[i]] += 1





# for r in range(R):
#     std[rec[r]] += 1
#     if len(q)<N:
#         q.append(rec[r])
#
# #             # q.append((std.index(max(std))))
#     else: # q 틀이 꽉 차면
#         # 현재 추천수 min 학생 아웃
#         out = 1001
#         for l in range(len(q)):
#             out = min(out, std[q[l]])
#
#         for l in range(len(q)):
#             if std[]
#             q.pop(out)
# print(q)
# # print(sorted(q))
