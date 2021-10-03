
def print_numbers(lower_limit,upper_limit):
    
    print("Even numbers:")
    for x in range(lower_limit,upper_limit):
        if x%2 == 0:
            print(x)
    
    print("Odd numbers:")
    for x in range(lower_limit,upper_limit):
        if x%2 != 0:
            print(x)

upper_limit=int(input("Enter upper limit:"))
lower_limit=int(input("Enter lower limit:"))
print_numbers(lower_limit,upper_limit)