def length_of_num(num):
  counter = 0

  for X in str(num):
    counter += 1
  return counter

print(length_of_num(2))
print(length_of_num(467))
print(length_of_num(475))