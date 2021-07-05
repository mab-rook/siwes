#fizzbuzz interview
question1 = int(input("enter number: "))

for question1 in range(1,20):
  if (question1 % 3 == 0):
    print('fizz')
  elif (question1 % 5 == 0):
    print('buzz')
  elif (question1 % 15 == 0):
    print('fizzbuzz')
  else:
    print(question1)