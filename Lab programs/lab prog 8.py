#wap to accept a string and returns a string havingfirst letter of each word in capital letter
#july 6
def practice():
    str1=input("enter a string: ")
    print("original string =",str1)
    str2=""
    x=str1.split()
    for a in x:
        str2+=a.capitalize() + ""
    print("Capitalized string:",str2)

practice()