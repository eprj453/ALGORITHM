import sys
sys.stdin = open('5110_input.txt', 'r')


class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

# def add(pre, data):
#     if pre == None:
#         print('error')
#     else:
#         pre.link = Node(data, pre.link)

def add(data, idx):
    global Head
    p = Head
    n = 0
    while n < idx-1:
        p = p.link
        n += 1
    p.link = Node(data, p.link)


def addtoLast(data): # 마지막에 데이터 삽입
    global Head

    if Head == None: # 빈 리스트라면
        Head = Node(data, None) # Head 하나 생성

    else:
        p = Head
        while p.link != None:
            p = p.link
        p.link = Node(data, None)


t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    Head = None
    list1 = list(map(int, input().split()))
    print(list1)
    for data in list1:
        addtoLast(data)
    for j in range(m-1):
        list2 = list(map(int, input().split()))

        print(list2)
        p = Head
        # result = False
        for k in range(len(list1)):
            result = False
            if list2[0] <= list1[0]:
                num = 0
                while num < len(list2):
                    add(list2[num], num)
                    num += 1
                break
            if list2[0] <= list1[k]:
                print(k)
                result = True
                num = k+1
                n = 0
                while num < k + len(list2)+1:
                    print(list2[n], num)
                    add(list2[n], num)
                    num += 1
                    n += 1
                break
        if result == False:
            n = 0
            for num2 in list2:
                addtoLast(num2)
                num += 1

        p = Head
        while p.link != None:
            print(p.data, end=' ')
            p = p.link
        print()
        # while num < 2:
        #     p = p.link
        #     num+=1




    num = 0
    p = Head
    while p.link != None:
        print(p.data, end=' ')
        p = p.link
    print()