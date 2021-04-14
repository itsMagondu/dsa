class Queue:
  def __init__(self):
    self.head = 0
    self.queue = []

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    item = self.queue[self.head]
    self.head += 1
    if self.head > len(self.queue): # split queue when bigger head is beyond halfway point
      self.queue = self.queue[self.head:]
      self.head = 0
    return item

  def __len__(self):
    return len(self.queue) - self.head

  def isempty(self):
    return len(self.queue) == self.head

# Testing
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print ('first dequeue:', q.dequeue())
print ('second dequeue:', q.dequeue())
print ('queue size:', q.__len__())
