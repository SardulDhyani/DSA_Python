# class LinearQueue:
#     def __init__(self):
#         self._queue = []
#     def isEmpty(self):
#         print(bool(len(self._queue)==0))
#     def enqueue(self, data):
#         self._queue.append(data)
#     def dequeue(self):
#         return self._queue.pop(0)
#     def size(self):
#         return len(self._queue)
#     def printall(self):
#         print(self._queue)
    
# if __name__ == "__main__":
#     queue = LinearQueue()
#     queue.isEmpty()
#     queue.enqueue(1)
#     queue.enqueue(2)
#     queue.enqueue(3)
#     queue.enqueue(4)
#     queue.enqueue(5)
#     # print(queue.printall())
#     queue.printall()
#     queue.dequeue()
#     queue.dequeue()
#     queue.dequeue()
#     queue.printall()
#     # print(queue.printall())

class LinearQueue(object):
    def __init__(self):
        self._queue = []
    def enqueue(self, data):
        self._queue.insert(0, data)
        return '{} added to the queue'.format(data)
    def dequeue(self):
        return '{} popped from the queue'.format(self._queue.pop())
    def queueSize(self):
        return 'Current size of queue is {}'.format(len(self._queue))
    
if __name__ == "__main__":
    queue = LinearQueue()
    print(queue.enqueue(1))
    print(queue.enqueue(2))
    print(queue.enqueue(3))
    print(queue.enqueue(4))
    print(queue.enqueue(5))
    print(queue.queueSize())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.queueSize())