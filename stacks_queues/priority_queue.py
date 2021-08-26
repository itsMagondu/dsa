# This DS stores values have have similar attributes and thus can be compared to each other.
# Uses a miminum binary heap

class Heap:
  def __init__(self):
    self.heap = [''] # initiliaze with sentinel item to make indexing easier. Or use a dict with indexes as keys?

  def insert(self, item):
    self.heap.append(item)
    self.rebalance_up()

  def remove(self):
    item = self.heap.pop(0) # What is I swap elements then POP since I will delete anyway?
    self.rebalance_down()
    return item
  
  def size(self):
    return len(self.heap)

  def get_heap(self):
    return self.heap

  def swap_insert(self, position):
    if self.size() <= 1:
      return

    if position == 0:
      return self.heap
    
    if position > self.size():
      return self.heap

    temp = self.heap[position]
    self.heap[position] = self.heap[position//2]
    self.heap[position//2] = temp
    
    self.swap_insert(position//2)

  def swap_delete(self, position):
    if self.size() <= 1:
      return

    # Check if the parent has children
    # Check if parent smaller than any of its children.
    # Swap with smallest child.
    if (position * 2) > self.size() and (position * 2 + 1) > self.size():
      # parent has no children. Return
      return
       
    left_child = position*2
    right_child = position*2+1

    # find greatest child. Compare with parent and swap the greatest child.

    # If right child does not exist, just compare left child with parent.
    if right_child >= self.size():
        if self.heap[left_child] > self.heap[position]:
          temp = self.heap[position]
          self.heap[position] = self.heap[left_child]
          self.heap[left_child] = temp

          self.swap_delete(left_child)
    elif self.heap[left_child] > self.heap[position] and self.heap[left_child] > self.heap[right_child]:
      temp = self.heap[position]
      self.heap[position] = self.heap[left_child]
      self.heap[left_child] = temp
      self.swap_delete(left_child)
    elif self.heap[right_child] > self.heap[position] and self.heap[right_child] > self.heap[left_child]:
      temp = self.heap[position]
      self.heap[position] = self.heap[right_child]
      self.heap[right_child] = temp
      self.swap_delete(right_child)

  def rebalance_up(self):
    # start index at 1 for these.
    # parent = current_index of item // 2
    # child_left = current_index * 2
    # child_right = current_index * 2 + 1
    heap_len = self.size()

    # Heap is either empty or has 1 item. No need to do anything.
    if heap_len <= 1:
      return

    else: 
      # is new item larger than its parent? If yes, swap.
      self.swap_insert(heap_len-1)

  def rebalance_down(self):
    heap_len = self.size()

    # Heap is either empty or has 1 item. No need to do anything.
    if heap_len <= 1:
      return

    else: 
      # is new item larger than its parent? If yes, swap.
      self.swap_delete(0)


h = Heap()
h.insert(1)
h.insert(3)
h.insert(2)
h.insert(4)
print("heap: ", h.get_heap())