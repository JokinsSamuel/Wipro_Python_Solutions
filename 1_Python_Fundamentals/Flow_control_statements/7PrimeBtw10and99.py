for num in range(10, 100):
  flag = 0
  for i in range(2,num):
    if (num%i) == 0:
      flag = 1

  if flag == 0:
    print(num)
  