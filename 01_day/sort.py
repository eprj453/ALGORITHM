# 버블 정렬
list1 = [5,66,19,54,21]

for i in range(len(list1)-1, 0, -1):
    for j in range(0, i):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print(list1)

# 카운팅 정렬

list2 = [0,1,0,4,0,3,1,3,2,0] # 정렬해보자

list_ex = [0]*5 # 카운팅 정렬을 하기 위해서는 최대값 정수의 크기만큼의 리스트가 필요하다. 0부터 4까지의 정수가 있으므로 5칸짜리 리스트 선언.

# 1. 각 정수의 빈도수를 인덱스로 저장
# ex. list_ex의 0번째에는 list2의 0의 갯수, 1번째에는 list2의 1의 갯수 .....

for i in list2:
    list_ex[i] += 1

print(list_ex)

for i in range(1, len(list_ex)):
    list_ex[i] = list_ex[i] + list_ex[i-1]
print(list_ex)

# 현재 상황
# list2 = [0,1,0,4,0,3,1,3,2,0]
# list_ex = [4, 6, 7, 9, 10]

# 정렬하기 위한 새로운 리스트 temp 선언(길이는 list2와 동일)
temp = [0] * len(list2)

# list2의 끝부터 temp에 집어넣는다.
# 만약 list2의 원소가 0이라면 list_ex의 0번째를 하나 감소.
# 만약 list2의 원소가 1이라면 list_ex의 1번째를 하나 감소.

for i in range(len(list2)-1, 0, -1):
    list_ex[list2[i]] -= 1
    temp[list_ex[list2[i]]] = list2[i]

print(list_ex)
print(temp)
