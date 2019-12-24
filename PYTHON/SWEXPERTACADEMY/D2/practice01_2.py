rank = 1
group_list = [[[0]*4]*6] # 조 6개
for i in range(0, 4):  # k = 6
    for j in range(0, 6):  # n = 4
        print(j - ((2*j)-5) * (i % 2), i)
        #group_list[j + (3 - j) * (i % 2)][i] = rank  # 짝수일때 정순 홀수일때 역순
        rank += 1

print(group_list)