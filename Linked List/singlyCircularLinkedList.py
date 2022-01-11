class Node:
    def __init__(self, node):
        self.data = node
        self.next = None
        self.prev = None
def insert(head, data):
    currentNode = head
    newNode = Node(0)
    if newNode == Node:
        print("Memory Error")
        return None
    newNode.data = data
    if head == None:
        newNode.next = newNode
        head = newNode
        return head
    else:
        while currentNode.next != head:
            currentNode = currentNode.next
        newNode.next = head
        currentNode.next = newNode  
    return head
def display(head):
    currentNode = head
    if head == None:
        return
    while True:
        print(currentNode.data, end=" ")
        currentNode = currentNode.next
        if currentNode == head:
            break
        
def length(head):
    currentNode = head
    count = 0
    if head == None:
        print("No Head Nodes")
        return 0
    else:
        while True:
            currentNode = currentNode.next
            count += 1
            if currentNode == head:
                break
    return count
def deleteFirst(head):
    prevNode = head
    next = head
    if head == None:
        return None
    if prevNode.next == prevNode:
        head = None
        return None
    while  prevNode.next != head:
        prevNode = prevNode.next
        next = prevNode.next
    prevNode.next = next.next
    head = prevNode.next
    
    return  head
def deleteLast(head):
    currentNode = head
    temp = head
    prevNode = None
    if head == None:
        return None
    if currentNode.next == currentNode:
        head = None
        return None 
    while currentNode.next != head:
        prevNode = currentNode
        currentNode = currentNode.next
    
    prevNode.next = currentNode.next
    head = prevNode.next
    return head

head = None 
head = insert(head, 9)
head = insert(head, 1)
head = insert(head, 2)
head = insert(head, 3)
head = insert(head, 4)
head = insert(head, 5)
print("Value Added are")
display(head)
head  = deleteFirst(head)
head = deleteLast(head)
print("\nValue After Deleting first and last element")
display(head)