# #Title: This the Mail-Room1 script
# # Change log (Who,When,What)
# #bshahabi,02/03/2019,Created the file"


#Adding New User and generate report

def add_new_user():
  dicdonor1 = {"Name": "William Gates", "Total": "653,772", "Gift Number": "2", "Average": "300000"}
  dicdonor2 = {"Name": "Jeff Bezos", "Total": "1000,000", "Gift Number": "5", "Average": "500000"}
  dicdonor3 = {"Name": "Paul Allen", "Total": "500,000", "Gift Number": "2", "Average": "100000"}
  dicdonor4 = {"Name": "Mark Zuckerberg", "Total": "800,000", "Gift Number": "2", "Average": "400000"}
  dicdonor5 = {"Name": "Michael Dell", "Total": "400,000", "Gift Number": "2", "Average": "200000"}
  dicData = {}

  Name = input("Enter the name:")
  Total = input("Enter the the total given:")
  Number = int(input('Enter the number of gifts:'))
  Average= int(input('Enter the average:'))
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
 #add_new_user()


def send_greeting():
 dicdonor1 = {"Name": "William Gates", "Total": "653,772", "Gift Number": "2", "Average": "300000"}
 dicdonor2 = {"Name": "Jeff Bezos", "Total": "1000,000", "Gift Number": "5", "Average": "500000"}
 dicdonor3 = {"Name": "Paul Allen", "Total": "500,000", "Gift Number": "2", "Average": "100000"}
 dicdonor4 = {"Name": "Mark Zuckerberg", "Total": "800,000", "Gift Number": "2", "Average": "400000"}
 dicdonor5 = {"Name": "Michael Dell", "Total": "400,000", "Gift Number": "2", "Average": "200000"}

 while (True):
   str = input('Enter the donar name with capital letter for first letter of name and last name (you can exit with typing 4):')
   if str == 'William Gates':
    print("Thank you Mr."+(dicdonor1["Name"]))
   elif str == 'Jeff Bezos':
    print("Thank you Mr."+(dicdonor2["Name"]))
   elif str == 'Mark Zuckerberg':
    print("Thank you Mr."+(dicdonor3["Name"]))
   elif str == 'Paul Allen':
    print("Thank you Mr.Allen"+(dicdonor4["Name"]))
   elif str == 'Michael Dell':
    print("Thank you Mr."+(dicdonor5["Name"]))
   elif str == "4":  # Exit with 0
    break


def send_letters_to_all():

        dicdonor1 = {"Name": "William Gates", "Total": "653,772", "Gift Number": "2", "Average": "300000"}
        dicdonor2 = {"Name": "Jeff Bezos", "Total": "1000,000", "Gift Number": "5", "Average": "500000"}
        dicdonor3 = {"Name": "Paul Allen", "Total": "500,000", "Gift Number": "2", "Average": "100000"}
        dicdonor4 = {"Name": "Mark Zuckerberg", "Total": "800,000", "Gift Number": "2", "Average": "400000"}
        dicdonor5 = {"Name": "Michael Dell", "Total": "400,000", "Gift Number": "2", "Average": "200000"}

        while (True):
            str = input(
                'Enter the donar name with capital letter for first letter of name and last name (you can exit with typing 4):')
            if str == 'William Gates':
                import tempfile
                tempfile.gettempdir()
                with open("William_Gates.txt",'w') as f:
                 f.write("Dear William,\n\n  Thank you for your kind donation of xxx.\n\n  It will be put to very goo")
                 f.close()

            elif str == 'Jeff Bezos':
                import tempfile
                tempfile.gettempdir()
                with open("Jeff_Bezos.txt", 'w') as f:
                 f.write('Dear Jeff Bezos,\n\n  Thank you for your kind donation of xxx.\n\n  It will be put to very good use.\n\n Sincerely, \n\n -The Team')
                f.close()

            elif str == 'Mark Zuckerberg':
                import tempfile
                tempfile.gettempdir()
                with open("Mark_Zuckerberg.txt", 'w') as f:
                 f.write('Dear Mark Zuckerberg,\n\n  Thank you for your kind donation of xxx.\n\n  It will be put to very good use.\n\n Sincerely, \n\n -The Team')
                f.close()

            elif str == 'Paul Allen':
                import tempfile
                tempfile.gettempdir()
                with open("Paul_Allen.txt", 'w') as f:
                 f.write('Dear Paul Allen,\n\n  Thank you for your kind donation of xxx.\n\n  It will be put to very good use.\n\n Sincerely, \n\n -The Team')
                f.close()

            elif str == 'Michael Dell':
                import tempfile
                tempfile.gettempdir()
                with open("Michael_Dell.txt", 'w') as f:
                 f.write('Dear Michael Dell,\n\n  Thank you for your kind donation of xxx.\n\n  It will be put to very good use.\n\n Sincerely, \n\n -The Team')
                f.close()
            elif str == "4":  # Exit with 0
                break


#User options

def user_selection():
 dicuser = {"1":"Send a Thank You to a single donor",
        "2":"Add a new user and create a Report",
        "3":"Send Letters to all donors",
        "4":"Quit"}
 [print(x + ":"+dicuser[x]) for x in dicuser]
 while True:
    try:
        a = int(input('Enter your choice from the above options:'))
        if a == 1:
            send_greeting()
        elif a == 2:
            add_new_user()
        elif a == 3:
            send_letters_to_all()
        elif a == 4:
            break
        else:
            raise ValueError
    except ValueError:
        print("Not a valid option! Please try again ...")


user_selection()