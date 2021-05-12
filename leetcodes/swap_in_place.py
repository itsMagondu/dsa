def swap_in_place(list):
  if len(list) < 2:
    return list
    
  len_list = len(list)
  midway = len_list // 2

  for i in range(midway):
    tmp = list[i]
    list[i] = list[(len_list-1)-i]
    list[(len_list-1)-i] = tmp

  print (list)
  return list

swap_in_place([1,2,3,4,5,6])
swap_in_place([1,2,3,4,5])

