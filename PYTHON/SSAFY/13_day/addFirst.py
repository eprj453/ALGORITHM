class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

# def addtoFirst(data):
#     global Head
#     Head = Node(data, Head)
#
# def addtoLast(data): # 마지막에 데이터 삽입
#     global Head
#     if Head == None: # 빈 리스트라면
#         Head = Node(data, None) # Head 하나 생성
#
#     else:
#         p = Head
#         while p.link != None:
#             p = p.link
#
#         p.link = Node(data, None)


# def add(pre, data):
#     if pre == Node:
#         print('error')
#     else:
#         pre.link = Node(data, pre.link)

data = [1,2,3,4]
Head = None
for i in range(len(data)):
    if i == len(data)-1:
        data[i] = Node(data[i], None)
    else:
        data[i] = Node(data[i], data[i+1])


for i in range(len(data)):
    print(data[i].data)
    print(data[i].link)

# while Head.link != None:
#     # print(Head.data, end=' ')
#     Head = Head.link
#     print(Head.link)
# print(Head.link)