import sys
sys.stdin = open('5108_input.txt', 'r')


class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link
#
def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)
#
def addtoLast(data): # 마지막에 데이터 삽입
    global Head

    if Head == None: # 빈 리스트라면
        Head = Node(data, None) # Head 하나 생성

    else:
        p = Head
        while p.link != None:
            p = p.link
        p.link = Node(data, None)
#
t = int(input())
for i in range(1, t+1):
    n, m, l = map(int, input().split()) # n > 배열 길이 m > 연산횟수 l > 찾을 인덱스
    data = list(map(int, input().split()))

    Head = None

    for j in range(len(data)):
        addtoLast(data[j])
        # print(Head.link)
    for j in range(m):
        idx, d = map(int, input().split())
        p = Head
        num = 0
        while num < idx-1:
            p = p.link
            num += 1
        add(p, d)

    p = Head.link
    for j in range(l-1):
        p = p.link
    print('#{} {}'.format(i, p.data))


#
# t = int(input())
# for i in range(1, t+1):
#     n, m, l = map(int, input().split())
#     data = list(map(int, input().split()))
#     for j in range(m):
#         s, d = map(int, input().split())
#         data.insert(s, d)
#     print('#{} {}'.format(i, data[l]))