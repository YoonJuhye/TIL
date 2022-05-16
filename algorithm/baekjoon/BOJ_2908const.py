A, B = map(int, input().split())

nA = int(str(A)[::-1])
nB = int(str(B)[::-1])


if nA > nB:
    print(nA)
else:
    print(nB)