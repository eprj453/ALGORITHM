string1 = input()
string2 = input()
l1, l2 = len(string1), len(string2)
check = [[0] * l1 for _ in range(l2)]

# for i in range(l1):
#     if string2[0] == string1[i]:
#        check[0][i] = 1
# for i in range(l2):
#     if string1[0] == string2[i]:
#       check[i][0] = 1

answer = 0
for i in range(0, l2):
    for j in range(0, l1):
        if string2[i] == string1[j]:
            check[i][j] = check[i-1][j-1]+1
            answer = max(answer, check[i][j])

print(answer)