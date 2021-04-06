# Create heap
x = [10,20,5,14,15,30,22,34,50]
heap = []

def swap_insert(position):
  if position == 0:
    return heap
  if heap[position//2] > heap[position]:
    return heap
  else:
    temp = heap[position]
    
    heap[position] = heap[position//2]
    heap[position//2] = temp
    swap_insert(position//2)

def swap_delete(position, heap_size):
  if heap_size == 0:
    return heap
  # Check if item is smaller than its children.
  child_right_index = position*2
  child_left_index = position*2+1

  # get largest child and swap with that child.
  if child_right_index <= heap_size and heap[position] < heap[child_right_index] and heap[child_right_index] > heap[child_left_index]:
    temp = heap[position]
    heap[position] = heap[child_right_index]
    heap[child_right_index] = temp
    swap_delete(child_right_index, heap_size)

  elif child_left_index <= heap_size and heap[position] < heap[child_left_index] and heap[child_left_index] > heap[child_right_index]:
    temp = heap[position]
    heap[position] = heap[child_left_index]
    heap[child_left_index] = temp
    swap_delete(child_left_index, heap_size)
  else:
    return heap

# Heap is a complete binary tree where the parent is always greater than all its descendants
def insert():
  for i,v in enumerate(x):
    if i == 0:
      heap.append(x[i])
    else:
      # get parent and check if this item is larger
      heap.append(v)
      parent = i//2
      if heap[parent] < heap[i]:
        # swap // make this recursive
        swap_insert(i)
  print ('created heap:', heap)

def delete():
  # Delete root node first then swap to get new largest node
  for i in range(len(heap)):
    # move largest item to the end
    # swap remaining items
    temp = heap[0]
    last = (len(heap)-1) - i
    heap[0] = heap[last]
    heap[last] = temp
    swap_delete(0,last-1)
  print ('sorted heap:', heap)

insert()
delete()