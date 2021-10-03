#WAP to count the number of words present in text files
#july 22

f=open("Lithika/story.txt","r")
str=f.read()
l=str.split()
c=0
for i in l:
    c=c+1

f.close()
print("total number of words =",c)