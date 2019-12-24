# 각 문자열의 길이는 30. 마디의 최대 길이는 10.
# 가장 첫 줄에는 테스트케이스 t
# 마디의 길이 출력

t = int(input())
for i in range(1,t+1):
    case = input()
    length = 1
    ans = 0
    for j in range(1,len(case)):
        if case[0:j] == case[j:j+length]:
           ans = length
           break
        else :
            length+=1
    print(f'#{i} {ans}') 


