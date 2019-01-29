# #Title: This a slicing script(with the last third, then first third, then the middle third in the new order)
# # Change log (Who,When,What)
# #bshahabi,1/25/2019,Created the file"

#The following script print the last and first third
def rt():
  srData = 'This is a test data for babak shahabi'
  a = srData[:3] #prints the first three characters
  b = srData[-3:]
  print(a + ' ' + b) # This prints the first and last three letters of the string
rt()

