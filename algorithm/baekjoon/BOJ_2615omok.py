

def find():
    ans = 0
    for i in range(19):
        for j in range(19):
            if pan[i][j] == 1:
                for k in range(4):
                    cnt1 = 1
                    ni = i + di[k]
                    nj = j + dj[k]
                    while 0<=ni<19 and 0<=nj<19 and pan[ni][nj] == 1:
                        cnt1 += 1
                        ni += di[k]
                        nj += dj[k]
                        # if cnt1 >= 6:
                        #     break
                        if cnt1 == 5:
                            if 0 <= ni < 19 and 0 <= nj < 19 and pan[ni][nj] == 1:
                                break
                            if 0 <= i - di[k] < 19 and 0 <= j - dj[k] < 19 and pan[i - di[k]][j - dj[k]] == 1:
                                break
                            else:
                                ans = 1
                            # ans = 1
                            return ans, i+1, j+1
            elif pan[i][j] == 2:
                for k in range(4):
                    cnt2 = 1
                    ni = i + di[k]
                    nj = j + dj[k]
                    while 0<=ni<19 and 0<=nj<19 and pan[ni][nj] == 2:
                        cnt2 += 1
                        ni += di[k]
                        nj += dj[k]
                        # if cnt2 >= 6:
                        #     break
                        if cnt2 == 5:
                            if 0 <= ni < 19 and 0 <= nj < 19 and pan[ni][nj] == 2:
                                break
                            if 0 <= i-di[k]<19 and 0 <= j-dj[k] < 19 and pan[i-di[k]][j-dj[k]]==2:
                                break
                            else:
                                ans = 2
                            # ans = 2
                            return ans, i+1, j+1
    return ans, 0, 0

pan = [list(map(int, input().split())) for _ in range(19)]
di = [0, 1, 1, -1]
dj = [1, 1, 0, 1]
ans, i, j = find()
if ans == 0:
    print(ans)
else:
    print(ans)
    print(i, j)

