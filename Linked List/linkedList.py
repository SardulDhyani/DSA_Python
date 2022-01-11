class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def insertStart(self, data):
        self.size += 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return "{} added to the begining of the Linked List".format(data)
    def sizeLL(self):
        return self.size
    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head
        while actualNode.next is not None:
            actualNode = actualNode.next
            
        actualNode.next = newNode
        return '{} added to the end of the Linked List'.format(data)
    
    def removeNode(self, data):
        if self.head is None:
            return
        self.size -= 1
        currentNode = self.head
        prevNode = None
        
        while currentNode.data != data:
            prevNode = currentNode
            currentNode = currentNode.next
            
        if prevNode is None:
            self.head = currentNode.next
        else:
            prevNode.next = currentNode.next
            return "Node {} is removed".format(data)
        
    def traverseLL(self):
        actualNode = self.head
        while actualNode != None:
            print("%d "%actualNode.data)
            actualNode = actualNode.next
                
                
if __name__ == "__main__":
    linkedList = LinkedList()
    print(linkedList.insertStart(4))
    print(linkedList.insertStart(3))
    print(linkedList.insertStart(2))
    print(linkedList.insertStart(1))
    print(linkedList.insertEnd(5))
    
    print("Linked List Size ", linkedList.sizeLL())
    linkedList.traverseLL()
    print(linkedList.removeNode(3))
    linkedList.traverseLL()