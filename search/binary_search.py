numbers = [1,2,3,4,5,6,8,9,10,11,12]

def search(look_for, list_numbers):
  if len(list_numbers) == 1:
    if look_for == list_numbers[0]:
      print (f'found in {list_numbers}')
    else:
      print ('not found')
  else:
    middle = len(list_numbers)//2
    if list_numbers[middle] == look_for:
      print (f'found in {list_numbers}')
    elif list_numbers[middle] < look_for:
      search(look_for, list_numbers[middle:])
    else:
      search(look_for, list_numbers[:middle])
    
search(4, numbers)
  