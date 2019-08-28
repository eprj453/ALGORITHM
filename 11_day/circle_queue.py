def isempty():
    return front == rear

def isFull():
    return (rear+1) % len(cQ) == front

def enQueue(item):
    global rear
    if isFull():
        print("Queue is full")
    else:
        rear = (rear + 1) % len(cQ)
        cQ[rear] = item


def deQueue():
    global front
    if isempty():
        print('Empty Queue')
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]


cQ_SIZE = 4
cQ = [0] * cQ_SIZE

front = rear = 0

enQueue('A')
enQueue('B')
enQueue('C')

print(deQueue())
print(deQueue())