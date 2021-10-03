#wap to count the number of vowels present in the file 
#july 22
f=open("d:/mytext.txt","r")
str=f.read()
vowel_count=0
for i in str:
    if i=='a' or i=='e' or i=='i' or i =='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        vowel_count=vowel_count+1

print("the number of vowels in text file:", vowel_count)

f.close()

