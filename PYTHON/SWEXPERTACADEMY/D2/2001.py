# 2001. 파리 퇴치
# n은 5 이상 15 이하, m은 2 이상 n 이하의 정수
t = int(input()) # 테스트 케이스
for i in range(0, t): # 테스트 케이스 갯수만큼 회전
    list2 = [] # int 형변환한 n 리스트를 저장할 n*n 리스트
    sum = 0 # 죽인 파리의 합을 저장하기 위한 변수 sum  
    nm = input() # n과 m을 입력
    nm2 = nm.split(' ') # n과 m을 분리해 각각 리스트에 저장
    print(f'nm2 : {nm2[0]}, {nm2[1]}')
    #print(int(nm2[0])-1)
    for j in range(0, int(nm2[0])): # 0부터 n번-1, 즉 리스트의 0번부터 n-1번까지 원소를 채우기 위해 회전(횟수는 n번만큼 회전)
        nn_list = input() # n*n 리스트의 첫번째줄 입력
        nn_list2 = nn_list.split(' ') # 리스트 분리해서 nn_list2에 저장
        list = [] # n 리스트를 int형변환 해 저장할 빈 리스트
        
        for k in range(0, len(nn_list2)):
            list.append(int(nn_list2[k]))
        # print(list)
        list2.append(list)
         # n*n 정수형 리스트 list2 완성.
    print(list2)
    max = 0
    # for l in range(0, int(nm2[0])-int(nm2[1])+1): #6칸 배열에서 2*2 파리채라면 가로로 5번, 7칸 배열에서 3*3 파리채라면 가로로 5번
    #     sum = 0
    #     q = 0
    #     max+=1
    #     for m in range(l, l+int(nm2[1])):  # 이 3칸의 반복문이 한번 다 돌아야 m*m 파리채의 파리 합이 구해진다. 
    #       for n in range(q, q+int(nm2[1])):#
    #         sum = sum + list2[m][n]
    #         print(f'{m},{n}칸의 값은 {list2[m][n]}')
    #       q+=1  
    #     print(f'칸 합계는 {sum}')
    #     if sum > max:
    #       max = sum
    #     #print(f'합계는 {sum}')
    # print(f'가장 큰 값은 {max}')
    
    for l in range(0,int(nm2[0])-int(nm2[1])+1):
      for m in range(0,int(nm2[0])-int(nm2[1])+1):
        sum = 0
        for n in range(l,int(nm2[1])+l):
          for o in range(m,int(nm2[1])+m):
            print(f'{n},{o}')
            sum = sum + list2[n][o]
        print(f'이번 칸의 합계는 {sum}')
        print('====')
        if sum > max:
          max = sum

    print(f'{i+1} {max}') 


    

    # n=5,m=3의 경우
    
    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5
    # 1 2 3 4 5

    # 00 01 02    10 11 12    20 21 22
    # 10 11 12    20 21 22    30 31 32
    # 20 21 22    30 31 32    40 41 42
    
    # 01 02 03    11 12 13    21 22 23
    # 11 12 13    21 22 23    31 32 33
    # 21 22 23    31 32 33    41 42 43
    
    # 02 03 04    12 13 14    22 23 23   
    # 12 13 14    22 23 24    32 33 34  
    # 22 23 24    32 33 34    42 43 44

    # 00 01 
    # 10 11
    
    # 01 02 
    # 11 12
    
    # 02 03 
    # 12 13
    
    # 03 04 
    # 13 14