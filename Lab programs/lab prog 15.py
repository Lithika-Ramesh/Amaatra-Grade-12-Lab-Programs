#WAP to read a file count and print total words starting with 'A' or 'a'
#july 27
def fun():
    f=open("Lithika/lab.txt","r")
    d=f.read()
    c=0
    for i in d:
        if i[0]=="A" or i[0]=="a":
            c=c+1
    print("total numbers of A and a in lab.txt file is: ",c)

fun()