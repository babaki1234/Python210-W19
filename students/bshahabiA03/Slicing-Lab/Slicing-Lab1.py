# #Title: This a slicing script(first and last items exchanged"
# # Change log (Who,When,What)
# #bshahabi,1/25/2019,Created the file"

def exchange_first_last(strData):
 strOut = strData[-1:]+strData[1:-1]+strData[:1]
 print(strOut)
 return strOut


def assert_exchange(strData):
 exchange_first_last(strData)
 assert exchange_first_last(strData) == "khis is a test for Babat"

#call the function
assert_exchange("this is a test for Babak")


