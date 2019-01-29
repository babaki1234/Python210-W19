# #Title: This a slicing script(every other item removed"
# # Change log (Who,When,What)
# #bshahabi,1/25/2019,Created the file"
def er():
 srData = 'This is a test data for babak shahabi'
 b = ""
 for i in range(len(srData)):
      if (i%2)==0:
          b+= srData[i]
 print(b)

er()