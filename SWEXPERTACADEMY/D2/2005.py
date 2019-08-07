## 파스칼 삼각형을 만들어보자


t = int(input())
for i in range(1,t+1):
    case = int(input())
    print(f'#{i}')
    tri_list =[]
    for j in range(case):
        tri_list2 = list()
      #  print(f'j는 {j}')
        for k in range(0,j+1):
            tri_list2.append(k+1)
        tri_list.append(tri_list2)
   # print(tri_list)
   # print(f'tri_list 길이는 {len(tri_list)}')
    tri_list[0][0] = 1
    for n in range(1,len(tri_list)):
        print(f'n1은 {n}')
       #print(f'len(tri_list)은 {len(tri_list)}')
        for m in range(0,len(tri_list[n])-1): # 4
            print(f'n2은 {n}')
            tri_list[n][0] = 1
            tri_list[n][-1] = 1
            print(tri_list)
            print(f'n2은 {n}')
            print(f'n의 길이는 {len(tri_list[n])}')
            print(f'm은 {m}')
            if n >= 2:
                tri_list[n][m] = (tri_list[n-1][m-1]) + (tri_list[n-1][m])
    
    for l in range(0,case):
        for o in range(0,len(tri_list[l])):
            print(f'{tri_list[l][o]}', end=' ')