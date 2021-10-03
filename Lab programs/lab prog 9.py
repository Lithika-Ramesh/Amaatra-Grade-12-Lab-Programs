#display all frequency of all elemnts of a list
#july 6

def prac():
    l=[3,21,5,6,3,8,21,6]
    l1=[]
    l2=[]
    for i in l:
        if i not in l2:
            x=l.count(i)
            l1.append(x)
            l2.append(i)
    print("element \t\t frequency")
    for i in range(len(l1)):
        print(l2[i],"\t\t\t",l1[i])

prac()
