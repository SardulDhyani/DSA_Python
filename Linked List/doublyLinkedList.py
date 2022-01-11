class Node(object):
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    
class DoublyLL(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def insert(self, value):
        newNode = Node(value, None, None)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        
    def traverseLL(self):
        currentNode = self.head
        while currentNode:
            item = currentNode.value
            currentNode = currentNode.next
            yield(item)
    
    def printList(self):
        for node in self.traverseLL():
            print(node, end=", ")
    
    def delete(self, value):
        currentNode = self.head
        flag = False
        if self.head is None:
            print("Linked list is empty Please add data to the linked list")
        elif self.head.value == value:
            self.head = currentNode.next
            self.head.prev = None
            flag = True
        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            flag = True
        else:
            while currentNode:
                if currentNode.value == value:
                    currentNode.prev.next = currentNode.next
                    currentNode.next.prev = currentNode.prev
                    flag = True
                currentNode = currentNode.next
        if flag:
            self.count -= 1
            
if __name__ == "__main__":
    DLL = DoublyLL()
    
    # INSERT
    DLL.insert(1)
    DLL.insert(2)
    DLL.insert(3)
    DLL.insert(4)
    DLL.insert(5)
    DLL.insert(6)
    DLL.insert(7)
    DLL.insert(8)
    print("\nPrinting after inserting values 1 to 8")
    DLL.printList()
    
    # DELETE HEAD AND TAIL VALUES
    print("\nPrinting after deleting head value and tail values")
    DLL.delete(1)
    DLL.delete(8)
    DLL.printList()
    
    # DELETE VALUES
    print("\nPrinting after deleting  mid value 4 and 5")
    DLL.delete(4)
    DLL.delete(5)
    DLL.printList()