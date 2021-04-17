class ListNode:
  def __init__(self, data, link = None):
    self.data = data
    self.link = link

class LinkedList:
  def __init__(self):
      self.head = None
      self.tail = None

  def addFirst(self, item):
    self.head = ListNode(item, self.head)
    if self.tail is None: self.tail = self.head

  def addLast(self, item):
    if self.head == None:
      self.addFirst(item)
    else:
      self.tail.link = ListNode(item)
      self.tail = self.tail.link

  def removeFirst(self):
    item = self.head.data
    self.head = self.head.link
    if self.head is None: self.tail = None
    return item

  def removeLast(self):
    # This process is inneficient. Takes O(n) time.
    if self.head is self.tail:
      return self.removeFirst()
    else:
      currentNode = self.head
      while currentNode.link is not self.tail:
        currentNode = currentNode.link
      
      item = self.tail.data

      self.tail = currentNode
      self.tail.link = None

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
print ('\nremove last last of two item:', q.removeLast())
print ('\nremove last again with three item:', q.removeLast())
# print ('\nShould not find an item and thus throw error:', q.removeLast())
