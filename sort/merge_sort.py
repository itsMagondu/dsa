array = [13,6,10,5,4,8,5,9,12,3,7,1,2,0]

# Top down approach
def merge_sort(array, left, right):
  if left >= right:
    return
  
  print ('array: ', array, ' left: ', left, ' right: ', right)
  middle = (left + right)//2
  merge_sort(array, left, middle)
  merge_sort(array, middle+1, right)
  merge(array, left, right, middle)

def merge(array, left, right, middle):
  left_copy = array[left:middle+1]
  right_copy = array[middle+1:right+1]

  left_copy_index = 0
  right_copy_index = 0
  sorted_index = left
  print ('array 1: ', array)
  
  while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
    if left_copy[left_copy_index] <= right_copy[right_copy_index]:
      array[sorted_index] = left_copy[left_copy_index]
      left_copy_index += 1
    else:
      array[sorted_index] = right_copy[right_copy_index]
      right_copy_index += 1
    sorted_index += 1
  
  print ('array 2: ', array)

  while left_copy_index < len(left_copy):
    array[sorted_index] = left_copy[left_copy_index]
    left_copy_index +=1
    sorted_index += 1
  
  print ('array 3: ', array)

  while right_copy_index < len(right_copy):
    array[sorted_index] = right_copy[right_copy_index]
    right_copy_index +=1
    sorted_index += 1
  print ('array 4: ', array)

merge_sort(array, 0, len(array)-1)
print (array)