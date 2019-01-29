#Remove the fruits starting with "O"
lstRow01 = ["Apples","Pears","Oranges","Peaches"]
for i in lstRow01:
     if i.startswith('O'):
         lstRow01.remove(i)
         print(lstRow01)