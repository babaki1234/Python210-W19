def send_greeting(str):
 dicdonor1 = {"Name": "William Gates", "Total": "653,772", "Gift Number": "2", "Average": "300000"}
 dicdonor2 = {"Name": "Jeff Bezos", "Total": "1000,000", "Gift Number": "5", "Average": "500000"}
 dicdonor3 = {"Name": "Paul Allen", "Total": "500,000", "Gift Number": "2", "Average": "100000"}
 dicdonor4 = {"Name": "Mark Zuckerberg", "Total": "800,000", "Gift Number": "2", "Average": "400000"}
 dicdonor5 = {"Name": "Michael Dell", "Total": "400,000", "Gift Number": "2", "Average": "200000"}
 result = ""
 if str == 'William Gates':
    result = "Thank you Mr."+(dicdonor1["Name"]);
 elif str == 'Jeff Bezos':
    result = "Thank you Mr."+(dicdonor2["Name"]);
 elif str == 'Mark Zuckerberg':
    result = "Thank you Mr."+(dicdonor3["Name"]);
 elif str == 'Paul Allen':
    result = "Thank you Mr.Allen"+(dicdonor4["Name"]);
 elif str == 'Michael Dell':
    result = "Thank you Mr."+(dicdonor5["Name"]);
 return result

send_greeting('Michael Dell')

def add_new_user(name, total, number, average):
  dicdonor1 = {"Name": "William Gates", "Total": "653,772", "Gift Number": "2", "Average": "300000"}
  dicdonor2 = {"Name": "Jeff Bezos", "Total": "1000,000", "Gift Number": "5", "Average": "500000"}
  dicdonor3 = {"Name": "Paul Allen", "Total": "500,000", "Gift Number": "2", "Average": "100000"}
  dicdonor4 = {"Name": "Mark Zuckerberg", "Total": "800,000", "Gift Number": "2", "Average": "400000"}
  dicdonor5 = {"Name": "Michael Dell", "Total": "400,000", "Gift Number": "2", "Average": "200000"}
  dicData = {}

  Name = name
  Total = total
  Number = number
  Average= average
  dicData["Name"]=Name
  dicData["Total"]=Total
  dicData["Gift Number"]=Number
  dicData["Average"]=Average
  print(dicdonor1)
  print(dicdonor2)
  print(dicdonor3)
  print(dicdonor4)
  print(dicdonor5)
  print(dicData)
  return dicData

add_new_user("Paul Allen", "800,000", "3", "400000")