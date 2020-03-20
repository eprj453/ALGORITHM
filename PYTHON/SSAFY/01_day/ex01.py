# 버블 정렬
arr = [55, 7, 78, 12, 42]

n = len(arr)

for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)

# 선택 정렬
arr1 = [55, 7, 78, 12, 42]

# min_num = arr1[0]
for j in range(len(arr1)-1):
    min_index = j
    for i in range(j + 1, len(arr1)):
        if arr1[i] < arr1[min_index]:
            min_index = i

    arr1[j], arr1[min_index] = arr1[min_index], arr1[j]

print(arr1)

# 카운팅 정렬

data = [0, 4, 1, 3, 1, 2, 4, 1]

counts = [0] * 5  # 최대값 : 4

# for val in data:
#     counts[val] += 1
#
# sorted = []
# for i in range(len(counts)):
#     for j in range(counts[i]):
#         sorted.append(i)
#
# print(sorted)


# 최적화
# 최대 혹은 최소가 되는 경우를 찾는 문제

# 완전 검색
# 생각해볼수 있는 모든 경우의 수를 나열해보고 확인하는 기법

# 순열
# 서로 다른 것 중에 몇 개를 뽑아 한 줄로 나열하는 것

word = 'ABC'

n = len(word)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if k == i or k == j:
                continue
            print(word[i], word[j], word[k])





