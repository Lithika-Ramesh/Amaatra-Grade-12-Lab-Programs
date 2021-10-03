#wap  using user defined functions which accept a list havingeven number of elements and swaps the elements at adjacent position
# a=[10,20,30,40,50,60]
#a=[20,10,40,30,60,50]
#date of execution june 29
def fun(A):
    l=len(A)
    for i in range(0,l,2):
        tmp=A[i]
        A[i]=A[i+1]
        A[i+1]=tmp
    print(A)

A=eval(input("Enter a list: "))
if(len(A)%2==0):
    fun(A)
