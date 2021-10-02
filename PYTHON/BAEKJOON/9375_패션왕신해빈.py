n = int(input())

for _ in range(n):
    answer = 1
    cloth_dict = dict()
    m = int(input())
    for _ in range(m):
        cloth, category = input().split(' ')
        cloth_dict[category] = cloth_dict.get(category, set())
        cloth_dict[category].add(cloth)

    for value in cloth_dict.values():
        answer *= (len(value) + 1) # 하나의 카테고리에서 선택할 수 있는 모든 경우의 수를 곱해주기

    answer -= 1 # 하나도 입지 않는 경우가 있으므로 1 빼주기
    print(answer)