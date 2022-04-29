

N = int(input())
sumV = 0
for _ in range(N):
    S, A = map(int, input().split())
    sumV += A % S

print(sumV)