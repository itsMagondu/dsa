class Deque:
  def __init__(self):
    self.deque = []

  def addFirst(self, item):
    return self.deque.insert(0, item) # This is inneficient. Takes 0(n) time.

  def addLast(self, item):
    return self.deque.append(item)

  def removeLast(self):
    return self.deque.pop()

  def removeFirst(self):
    return self.deque.pop(0) # This is inneficient. Takes 0(n) time.

  def isEmpty(self):
    return len(self.deque) == 0

  def __len__(self):
    return len(self.deque)