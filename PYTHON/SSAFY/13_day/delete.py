def delete(pre):
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link

class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addtoFirst(data):
    global Head
    Head = Node(data, Head)

def delete(pre):
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link


def add(pre, data):
    if pre == Node:
        print('error')
    else:
        pre.link = Node(data, pre.link)

data = [1,2,3,4]
Head = None

for i in range(len(data)):
    addtoFirst(data[i])

add(Head, 8)

delete(Head)

while Head.link != None:
    print(Head.data, end=' ')
    Head = Head.link
print(Head.link)