numbers = [6,10,5,13,4,8,5,9,12,3,7,1,2,0]

numbers_count = len(numbers)

for n in range(numbers_count):
  smallest = numbers[n]
  position = n

  for num in range(n, numbers_count):
    if smallest > numbers[num]:
      smallest = numbers[num]
      position = num

  numbers[position] = numbers[n]
  numbers[n] = smallest
  print (numbers)
