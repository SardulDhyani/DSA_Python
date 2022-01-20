class Node(object):
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class CircularDoublyLL(object):
    def __init__(self) :
        self.head = None
        self.tail = None
        self.count = 0
    
    def insertStart(self, value):
        newNode = Node(value, None, None)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            self.tail = self.head
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            currentNode = self.head
            self.head = newNode
            self.head.next = currentNode
            self.head.prev = self.tail
            self.tail.next = self.head
        self.count += 1
    
    def insertEnd(self, value):
        newNode = Node(value, None, None)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            self.tail = self.head
            self.head.prev = self.tail
        else:
            newNode.prev = self.tail
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
            # self.tail.next = self.head
        self.count += 1
    
    def dislplayLL(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        else:
            currentNode = self.head
            while True:
                print(currentNode.value, end=", ")
                if currentNode.next == self.head:
                    break
                currentNode = currentNode.next
    def deleteNode(self, value):

        if self.head is None:
            print("Linked List is Empty")
            return
        flag = False
        prevNode = self.head
        currentNode = self.head
        while True:
            if currentNode.value == value:
                flag = True
                break
            if currentNode.next == self.head:
                break
            prevNode = currentNode
            currentNode = currentNode.next
            
        if flag:
            if currentNode == self.head:
                prevNode.next = currentNode.next
                currentNode.next.prev = prevNode
                self.head = currentNode.next
            else:
                prevNode.next = currentNode.next
                currentNode.next.prev = prevNode
            self.count -= 1
            return
        else:
            print("Value Not Availble in LL")
            
        
            
    
CDLL = CircularDoublyLL()
CDLL.insertStart(1)
CDLL.insertEnd(2)
CDLL.insertEnd(3)
CDLL.insertEnd(4)
CDLL.insertStart(0)
# CDLL.deleteNode(0)
CDLL.deleteNode(2)
CDLL.dislplayLL()
# CDLL.deleteNode(2)
# CDLL.dislplayLL()