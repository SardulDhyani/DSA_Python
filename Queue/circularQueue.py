class CircularQueue(object):
    def __init__(self, size):
        self.size = size
        self._queue = [None for i in range(size)]
        self.front = -1
        self.rear = -1
    def enqueue(self, data):
        if ((self.rear+1)%self.size == self.front):
            print("Queue is Full")
        elif(self.front == -1):
            self.front = 0
            self.rear = 0
            self._queue[self.rear] = data
        else:
            self.rear = (self.rear+1) % self.size
            self._queue[self.rear] = data
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
        elif self.front == self.rear:
            temp = self._queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self._queue[self.front]
            self.front = (self.front+1)%self.size
            return temp
    
    def display(self):
        if(self.front == -1):
            print("Queue is Empty")
        elif(self.rear >= self.front):
            print("Element in queue are: ", end="")
            for i in range(self.front, self.rear+1):
                print(self._queue[i], end =" ")
            print()
        elif((self.rear+1)%self.size == self.front):
            print("Element in queue are: ", end="")
            for i in range(self.front, self.size):
                print(self._queue[i], end=" ")
            for i in range(self.rear+1):
                print(self._queue[i], end=" ")
            
    def isEmpty(self):
        pass
    
if __name__ ==  "__main__":
    queue = CircularQueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print("Dequeue ",queue.dequeue())
    print("Dequeue ",queue.dequeue())
    print("Dequeue ",queue.dequeue())
    queue.display()
    print("Enqueue")
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.display()
