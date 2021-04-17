class ListNode:
  def __init__(self, data, forward = None, backward = None):
    self.data = data
    self.forward = forward
    self.backward = backward

class LinkedList:
  def __init__(self):
      self.head = None
      self.tail = None

  def addFirst(self, item):
    self.head = ListNode(item, self.head, self.tail)
    if self.tail is None: self.tail = self.head

  def addLast(self, item):
    if self.head == None:
      self.addFirst(item)
    else:
      self.tail.backward = ListNode(item, self.tail)
      self.tail = self.tail.backward

  def removeFirst(self):
    item = self.head.data
    self.head = self.head.backward
    if self.head is None: self.tail = None
    return item

  def removeLast(self):
    if self.head is self.tail:
      return self.removeFirst()
    else:
      item = self.tail.data

      self.tail = self.tail.forward
      self.tail.backward = None
      return item

# Testing
q = LinkedList()
q.addFirst(2)
print ('remove first with one item:', q.removeFirst())

q.addFirst(2)
print ('remove last with one item: ', q.removeLast())

q.addFirst(2)
q.addFirst(3) 
q.addLast(1)

print ('\nremove first of three item:', q.removeFirst())
print ('\nremove last of two item:', q.removeLast())
print ('\nremove last again with single item:', q.removeLast())
# print ('\nShould not find an item and thus throw error:', q.removeLast())
