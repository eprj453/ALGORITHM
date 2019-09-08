list1 = [[1,2],[3,4]]
list2 = []
for i in range(2):
    list2.append([])
    for j in range(2):
        list2[i].append(list1[i][j])
list2[0][1] = 5
print(list1)
print(list2)