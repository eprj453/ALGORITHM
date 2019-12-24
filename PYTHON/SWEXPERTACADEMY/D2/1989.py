# 문자열을 입력받아서 거꾸로 입력해도 동일한지 확인,
# 동일하면 1 반환, 동일하지 않으면 0 반환.

t = int(input())
for i in range(1,t+1):
    count = 0
    case = input()
    case.rstrip('\r')
    list1 = []
    list2 = []

    # for j in range(0,len(case)):
    #     list1.append(case[j])
    # for k in range(0,len(list1)):
    #     list2.append(list1[len(list1)-k-1])
    for l in range(0,len(case)):
        if case[l] != case[len(case)-l-1]:
            count+=1
        # elif case[l] != case[len(case)-l-1]:
        #     print(f'#{i} 0')
        #     break
    if count > 0:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')


        