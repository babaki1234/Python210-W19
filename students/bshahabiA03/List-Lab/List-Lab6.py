#Ask for favorite fruit
lstRow01 = ["Apples","Pears","Oranges","Peaches"]

str = input('Do you like apples?')
if str == "Yes":
    print('Here is an organic Apple for you ')
else:

    a = lstRow01.remove("Apples")
    print(lstRow01)