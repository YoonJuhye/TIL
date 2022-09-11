
def solution(new_id):
    new_id1 = new_id.lower()
    # print(new_id1)
    new_id2 = ''
    for i in range(len(new_id1)):
        if new_id1[i].islower() or new_id1[i].isdigit() or new_id1[i] == '-' or new_id1[i] == '_' or new_id1[i]=='.':
            new_id2 += new_id1[i]
            # if new_id1[i] =='.' and i >= 1 and new_id1[i-1] == '.':
            #     pass
            # else:
            #     new_id2 += new_id1[i]
    new_id3 = ''
    for j in range(len(new_id2)):
        if j > 0 and new_id2[j] == '.' and new_id2[j-1] == '.':
            continue
        else:
            new_id3 += new_id2[j]
    # print(new_id3)
    if new_id3[0] == '.': # 4단계
        if len(new_id3) >= 2:
            new_id3 = new_id3[1:]
    if new_id3[-1] == '.':
        new_id3 = new_id3[:-1]
    # print(new_id3)
    if new_id3 == '':
        new_id3 = 'a'
    if len(new_id3) >= 16:
        new_id3 = new_id3[:15]
        if new_id3[-1] == '.':
            new_id3 = new_id3[:14]
    if len(new_id3) <= 2:
        if len(new_id3) == 2:
            new_id3 += new_id3[-1]
        elif len(new_id3) == 1:
            new_id3 += new_id3[-1]
            new_id3 += new_id3[-1]
    answer = new_id3
    return answer