p = 'abcdef'

word = 'asdabjhcvbjabcdefnsdfbxcvikvksbc'

n, m = len(word), len(p) # n > 텍스트 길이, m > 패턴의 길이

for i in range(n-m+1):
    for j in range(m):
        if word[i+j] != p[j]:
            break
    else:
        print(word[i:i+m])