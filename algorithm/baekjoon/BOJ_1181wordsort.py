# N = int(input())
# lst = []
# for _ in range(N):
#     word = input()
#     lst.append(word)
# lst_a = set(lst)
# lst_b = []
# for i in lst_a:
#     lst_b.append(i)
# lst_b.sort(key=lambda x:(len(x), x))
# for i in lst_b:
#     print(i)
N = int(input())
lst = []
for _ in range(N):
    word = input()
    lst.append(word)
lst.sort(key=lambda x:(len(x), x))
result = set(lst)
# lst_a = set(lst)
# lst_b = []
# for i in lst_a:
#     lst_b.append(i)
# lst_b.sort(key=lambda x:(len(x), x))
for i in result:
    print(i)
