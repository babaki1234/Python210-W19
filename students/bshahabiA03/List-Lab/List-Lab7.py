#Make the item reverse and remove the last one
lstRow01 = ["Apples","Pears","Oranges","Peaches"]
lstRow02 = [lstRow01[0][::-1],lstRow01[1][::-1],lstRow01[2][::-1],lstRow01[3][::-1]]
print(lstRow02)
lstRow03 = lstRow01[:-1]
print(lstRow01)
print(lstRow03)