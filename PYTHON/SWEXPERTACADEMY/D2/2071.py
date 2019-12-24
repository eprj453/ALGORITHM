
# 2071. 평균값 구하기
# 10개의 수를 입력받아 평균값을 구한다

t = int(input())

for i in range(1,t+1):
    list = []
    sum = 0
    case = input()
    case2 = case.split(' ')
    for j in range(0,len(case2)):
        list.append(int(case2[j]))
    for k in list:
        sum = sum + k
    print(list)
    avg = sum / len(list)
    print(f'#{i} {round(avg)}') 
# 1984 . 중간값 구하기

# 10개의 수를 입력받아 최대 수와 최소 수를 제외한 나머지 수의 평균값을 구하는 프로그램 작성.
t = int(input())
for i in range(1, t+1):
    case = input()
    case2 = case.split(' ')
    print(case2)
    sum = 0
    list = []
    for j in case2:
        list.append(int(j))
    print(list)
    max_num = max(list)
    min_num = min(list)
    len_list = len(list)
    for k in list:
        if k != max_num and k != min_num:
            sum = sum + k
        else:
            len_list -= 1
    print(f'#{i} {int(sum / len)}')




    
        

