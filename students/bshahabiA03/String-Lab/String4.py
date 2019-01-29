#Prints some row and columns

for students in (('Bob', '+A', '2'), ('Susan', 'A', '2'),('James','+B','3')):
  print('{0:<10} {1:>8} {2:>8}'.format(*students))