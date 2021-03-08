numbers = [13,6,10,5,4,8,5,9,12,3,7,1,2,0]

for x in range(len(numbers)-1, 0, -1):
  for n in range(x):
    if numbers[n] > numbers[n+1]:
      temp = numbers[n]
      numbers[n] = numbers[n+1]
      numbers[n+1] = temp
  print (numbers)

print (f'final list {numbers}')