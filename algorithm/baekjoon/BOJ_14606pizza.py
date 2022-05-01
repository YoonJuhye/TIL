def dp1(n):
    dp = [0] * 11
    dp[1] = 0
    dp[2] = 1
    for i in range(3, n+1):
        l = i // 2
        dp[i] = l*(i-l)+dp[l]+dp[i-l]
    return dp[n]

N = int(input())
print(dp1(N))