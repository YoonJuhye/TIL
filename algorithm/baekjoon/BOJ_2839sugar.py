# N = int(input())
'''
3A+5B = N
A+B 최소값 출력
정확하게 Nkg 안되면 -1 출력
'''
# for k in range(1, (N//2)+1):
#     if 5*(N-k) + 3*k == 15*N or 3*(N-k) + 5*k == 15*N:
#         print(min(N))
#     else:
#         print(-1)

n = int(input()) # 설탕

result = 0 # 봉지 수

while n >= 0:
    if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
        result += n // 5 # 5로 나눈 몫 추력
        print(result)
        break
    n -= 3 # 설탕이 5의 배수가 될때까지 반복
    result += 1 # 봉지 추가
else:
    print(-1) # while문이 거짓이 되면 -1 출력