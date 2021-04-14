# partition list based on some number. Sort two parts
unsorted_list = [7,4,3,8,1,5,9,6,2,0]
unsorted_list.append(999)

high = len(unsorted_list)-1
low = 0

def quicksort(low, high):
  if low < high:
    j = partition(low, high)
    quicksort(low, j)
    quicksort(j+1, high)

def partition(low, high):
  pivot = unsorted_list[low]
  i = low
  j = high

  while i < j:
    i+=1
    while unsorted_list[i] < pivot:
      i += 1
  
    j-=1
    while unsorted_list[j] > pivot:
      j -= 1

    if i < j:
      temp = unsorted_list[i]
      unsorted_list[i] = unsorted_list[j]
      unsorted_list[j] = temp

  unsorted_list[low] = unsorted_list[j]
  unsorted_list[j] = pivot
  return j

quicksort(low, high)
print (unsorted_list)
