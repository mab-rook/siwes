chicken = 2
cows = 4
pigs = 4

animal = [2, 3, 5]
total_of_animal = [2,4,4]
times = []
for num1, num2 in zip(animal, total_of_animal):
  times.append(num1*num2)

print(sum(times))
