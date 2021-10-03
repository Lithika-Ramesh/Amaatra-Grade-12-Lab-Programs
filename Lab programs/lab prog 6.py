# wap a program to check wether the entered number is perfect number or not using user defined function
# the sum of factors for the given number must be equal the number entered
#date of e : july 29 
def perf(n):
    sum=0
    for i in range(1,n):
        if ((n%i) == 0):
            sum=sum+i
    return sum
    
n=int(input("enter a number: "))
s=perf(n)
#print(s)
#print(n)
if n==s:
    print("it is a perfect number")
else:
    print("its not a perfect number ")



                
