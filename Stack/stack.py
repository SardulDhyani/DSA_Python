# class Stack:
#     def __init__(self):
#         self._items = list()
#     def isEmpty(self):
#         return len(self) == 0
#     def __len__(self):
#         return len(self._items)
#     def peek(self):
#         assert not self.isEmpty(), print("Cannot peek as stack is empty")
#         return self._items[-1]
#     def pop(self):
#         assert not self.isEmpty(), "Cannot peek as stack is empty"
#         return self._items.pop()
#     def push(self, item):
#         self._items.append(item)
    
# s = Stack()
# s.push(1)
# s.push(2)
# print("Peek ",s.peek())
# s.push(3)
# s.push(4)
# print("Print ", s._items)
# print("Len ",s.__len__())
# print(s.peek())
# print(s.__len__())
# print(s.peek())
# print(s.peek())
# print(s.peek())

class Stack(object):
    def __init__(self):
       self.stack = []
       self.numberofitem =0
    def push(self, data):
        self.stack.insert(self.numberofitem, data)
        self.numberofitem += 1
        return '{} pushed into stack'.format(data)
    def pop(self):
        self.numberofitem -= 1
        data = self.stack.pop(self.numberofitem)
        return '{} popped from stack'.format(data)
    def stackSize(self):
        return 'Current size of Stack is {}'.format(len(self.stack))

if __name__ == "__main__":
    stack = Stack()
    print(stack.push(1))
    print(stack.push(2))
    print(stack.push(3))
    print(stack.push(4))
    print(stack.stackSize())
    print(stack.pop())
    print(stack.pop())
    print(stack.stackSize())