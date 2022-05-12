
num = list(map(int, input().split()))
# print(num)
sumV = 0
for i in range(len(num)):
    sumV += num[i]**2
sol = sumV % 10
print(sol)