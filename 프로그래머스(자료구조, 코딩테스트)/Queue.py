class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def add(self, data):
        new_item = Node(data)
        if not self.first: # 비어있는 Queue라면
            self.first = new_item
            self.last = self.first
        else:
            self.last.next = new_item
            self.last = self.last.next
        self.length += 1

    def pop(self):
        if not self.first:
            raise ValueError

        data = self.first
        self.first = self.first.next

        if not self.first:
            self.last = None
        self.length -= 1
        return data.data

    def get(self):
        if not self.first:
            raise ValueError
        return self.first.data

    def traverse(self):
        arr = []
        start = self.first
        while start:
            arr.append(start.data)
            start = start.next
        return arr



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

q = Queue()
q.add(1)
q.add(3)
q.add(2)
print("queue 순회 : ", q.traverse())
print("queue 첫번째 : ",  q.get())
print("queue에서 원소 2개 빼기")
q.pop()
q.pop()
print("queue에서 원소 2개 뺀 후 : ", q.traverse())