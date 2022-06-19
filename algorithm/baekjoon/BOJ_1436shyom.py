n = int(input())
cnt = 0
s = 1
while True:
    if '666' in str(s):
        cnt += 1
    if cnt == n:
        print(s)
        break
    s += 1