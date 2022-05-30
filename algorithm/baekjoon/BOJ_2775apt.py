# 부녀회장이 될테야
T = int(input())
# k: 층 n: 호
for t in range(1, T+1):
    k = int(input())
    n = int(input())

    # 1, 3 1층의 3호에 살려면
    # 0층의 1호부터 3호까지
    # 사람들의 수의 합만큼 사람들을 데려와 살아야 함
    # 0층의 i호에는 i 명 [0][i] => i [1][i] => i(i+1)/2 [2][i] => [1][i]+[2][i-1]
    # [k][0]은 무조건 1
    # [[1, 2, 3 ,,,, 14], #0층
    # [1,1+2,1+2+3,,,i(i+1)/2], #1층
    # [1,1+(1+2),1+(1+2)+(1+2+3),], #2층
    # [1,i] # k층 n호 = [k-1][n]+[k][n-1]
    # [1,,]] # 14층

    apt = [[0] * 15 for _ in range(k)]
    # print(arr)
    for i in range(k):
        for j in range(15):
            if i == 0:
                apt[i][j] += j + 1
            else:
                apt[i][j] = apt[i-1][j]+apt[i][j-1]

    print(apt)
    print(apt[k][n-1])






