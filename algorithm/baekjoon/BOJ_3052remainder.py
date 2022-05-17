lst = []
for _ in range(10):
    A = int(input())
    C = A % 42
    lst.append(C)

print(len(set(lst)))