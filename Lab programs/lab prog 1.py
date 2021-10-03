
def positive(x,y):
    ans = x**3 + (3*x**2*y)+ (3*x*y**2) + y**3
    return ans

def negative(x,y):
    ans = x**3 - (3*x**2*y) + (3*x*y**2) - y**3
    return ans

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

sign = str (input("Enter \"+\" for (a+b)^3 or \"-\" for (a-b)^3:"))
if (sign == "+"):
    ans=positive(x,y)
    print("The answer is:",ans)
    
elif (sign == "-"):
    ans=negative(x,y)
    print("The answer is:",ans)

else:
    print("That is an invalid choice. Please choose between \"+\" and \"-\".")