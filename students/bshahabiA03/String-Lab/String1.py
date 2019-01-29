#Title: This the string format exercise
# Change log (Who,When,What)
#bshahabi,1/27/2019,Created the file"

tplDataRow01 = (2, 123.4567, 10000, 12345.67)
tplDataRow02 = 'file_{:>03d}:'.format(tplDataRow01[0],'{0:.2f}'.format(tplDataRow01[1]))
tplDataRow03 = "{:.2E}".format(tplDataRow01[2]),'%.2e'%(tplDataRow01[3])
tplDataRow04 = '%.2e'%(tplDataRow01[3])
print(tplDataRow02, tplDataRow03,tplDataRow04)
