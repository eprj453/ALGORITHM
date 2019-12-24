
my_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
           '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
           'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
           }

for i in range(1, int(input())+1):
    n, num = map(str, input().split())
    ans = ''
    for j in range(int(n)):
        ans += my_dict[num[j]]
    print('#{} {}'.format(i, ans))