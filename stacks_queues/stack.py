class Stack:
  def __init__(self):
    self.stack = []
  def pop(self):
    # Need to implement this without using pop
    return self.stack.pop()

  def push(self, item):
    self.stack.append(item)
  def peek(self):
    return self.stack[-1]
  def __len__(self):
    return len(self.stack)

  def isempty(self):
    return len(self.stack) == 0

# Testing
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print ('first pop:', s.pop())
print ('second pop:', s.pop())
print (s.__len__())