# #Title: This the Mail-Room1 script
# # Change log (Who,When,What)
# #bshahabi,1/27/2019,Created the file"
tplDatadonor1 = ("William Gates", "653,772","2","300000")
tplDatadonor2 = ("Jeff Bezos", "1000,000","5","500000")
tplDatadonor3 = ("Paul Allen", "500,000","2","100000")
tplDatadonor4 = ("Mark Zuckerberg", "800,000","2","400000")
tplDatadonor5 = ("Michael Dell", "400,000","2","200000")
tplDataTableA = (tplDatadonor1,tplDatadonor2,tplDatadonor3,tplDatadonor4,tplDatadonor5)
def send_geeting():
     while(True):
         str = input('Enter the donar name:')
         if str == 'William Gates':
             print("Thank you Mr. %s"%(tplDatadonor1[0]))
         elif str == 'Jeff Bezos':
             print("Thank you Mr.%s"%(tplDatadonor2[0]))
         elif str == 'Mark Zuckerberg':
             print("Thank you Mr.%s"%(tplDatadonor4[0]))
         elif str == 'Paul Allen':
             print("Thank you Mr.Allen.%s"%(tplDatadonor3[0]))
         elif str == 'Michael Dell':
             print("Thank you Mr.Dell.%s"%(tplDatadonor5[0]))
         elif str == "0": #Exit with 0
           break


def add_new_user():
    tplDatadonor1 = ("William Gates", "653,772", "2", "300000")
    tplDatadonor2 = ("Jeff Bezos", "1000,000", "5", "500000")
    tplDatadonor3 = ("Paul Allen", "500,000", "2", "100000")
    tplDatadonor4 = ("Mark Zuckerberg", "800,000", "2", "400000")
    tplDatadonor5 = ("Michael Dell", "400,000", "2", "200000")
    tplDataTableA = (tplDatadonor1, tplDatadonor2, tplDatadonor3, tplDatadonor4, tplDatadonor5)

    Name = input('Enter the name:')
    Total = input('Enter the the total given:')
    Gift = int(input('Enter the number of gifts:'))
    Average= int(input('Enter the average:'))

    tplData = (Name,Total,Gift,Average),
    tplDataTableA += tplData
    print('---------------')
    for row in tplDataTableA:
            print("Donor Name | Total Given in $US | Num Gifts | Average in $US")
            print("------------------------------------------------------------")
            print('{:>8} {:>13} {:>11} {:>16}'.format(*row))

def list():
      str1 = input('Enter the statement:')
      if str1 == 'List':
        print ("This is the list of all donors:",(tplDatadonor1[0],tplDatadonor2[0],tplDatadonor3[0],tplDatadonor4[0],tplDatadonor5[0]))

def user_options():
    n = int(input("Enter number 1 to send a Thank you, enter 2 to show the list of donors,enter 3 to add a new user the list and generates a report:"))
    if n == 1:
        send_geeting()
    elif n == 2:
        list()
    elif n == 3:
        add_new_user()
user_options()
