#wap to read and display contents of marks.dat
#date: 26 8 21

f= open("marks.dat", 'r')
while str:
    str= f.readline()
    print(str)
f.close()