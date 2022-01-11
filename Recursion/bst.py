class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def Search(root, key):
    while root != None:
        if key > root.data:
            root = root.right
        elif key < root.data:
            root = root.left
        else:
            return True
    return False

def Insert(Node, data):
    if Node == None:
        return newNode(data)
    if data < Node.data:
        Node.left = Insert(Node.left, data)
    elif data > Node.data:
        Node.right = Insert(Node.right, data)
    return Node

if __name__ == "__main__":
    root = None
    root = Insert(root, 50)
    Insert(root, 20)
    Insert(root, 60)
    Insert(root, 30)
    Insert(root, 10)
    if Search(root, 60):
        print("60 is availble")
    else:
        print("60 is not availble")