#Title: This a slicing script("with the first 4 and the last 4 items removed, and then everyother item"
# Change log (Who,When,What)
#bshahabi,1/25/2019,Created the file"

def er4():
 srData = 'This is a test data for babak shahabi'

 a = srData[4:-4] #This removes the first and last 4 items#
 print(a)
 c = ""
 for i in range(len(a)):
  if (i%2)==0:
        c+= a[i]
 print(c)
er4()