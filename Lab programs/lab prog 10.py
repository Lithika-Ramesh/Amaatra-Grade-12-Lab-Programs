#WAP to display those strings which are starting with 'A' or 'a' of goiven string of list
#july 6
def prac():
    l=["Aryan","leena","akhil","reema"]
    count=0
    for i in l:
        if i[0] in ('aA'):
            count=count+1
            print(i)

prac()