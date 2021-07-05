secret_number = 10
i = 0
while i < 3:
  guess_number = int(input("guess a number: "))
  
  if guess_number == secret_number:
    print('you are correct')
    break

  print('you are not correct')
i += 1
  
  
  
