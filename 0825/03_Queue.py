def enQueue(Q,item):
    global rear
    if isFull(Q):
        print("Queue_Full")
    else:
        rear += 1
        Q[rear] = item


def deQueue(Q):
    global front
    if (isEmpty(Q)):
        print('Empty')
    else:
        front += 1
        return Q[front]


def isEmpty(Q):
    return front == rear


def isFull(Q):
    return rear == len(Q) - 1

def Qpeak(Q):
    if isEmpty(): print("Queue_Empty")
    else: return Q[front+1]


n = 5
Que = [0] * n
front = rear = -1
enQueue(Que,1)
enQueue(Que,2)
enQueue(Que,3)
print(deQueue(Que))
print(deQueue(Que))
print(deQueue(Que))