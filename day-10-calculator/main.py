
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

# num1 = float(input("Enter 1st value :\n >>  "))
# operation = str(input("Enter operation to perform \n+\n-\n/\n* \n  "))
# num2 = float(input("Enter 2nd value :\n >>  "))

# def calculation():
#     if operation == '+':
#         add(num1=num1, num2=num2)
#     elif operation == '-':
#         subtract(num1=num1, num2=num2)
#     elif operation == '*':
#         multiply(num1=num1, num2=num2)
#     elif operation == '/':
#         divide(num1=num1, num2=num2)
#     else:
#         print("Please enter correct operation")


# should_continue = True
# while should_continue:
    
#     num1 = int(input("Enter 1st value :\n >>  "))
#     operation = str(input("Enter operation to perform \n+\n-\n/\n* \n  "))
#     num2 = int(input("Enter 2nd value :\n >>  "))
    

    
#     calculation()

#     restart = str(input("\nDo you want to continue 'y', 'n': \n"))

#     if restart == 'n':
#         should_continue = False
#         print("GoodBye")


# 2nd Approach using a dictionary

ops = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide,
}
should_continue = True
while should_continue:
    num1 = float(input("Enter 1st value :\n >>  "))
    for symbol in ops:
        print(symbol)
    operation_symbol = str(input("Select the operation: "))
    num2 = float(input("Enter 2nd value :\n >>  "))
    print(f"{num1} {operation_symbol} {num2}: {ops[operation_symbol](num1,num2)}")

    restart = str(input("\nDo you want to continue 'y', 'n': \n"))

    if restart == 'n':
        should_continue = False
        print("GoodBye")