
def add(num1, num2):
    output = print(f"The addition of {num1} and {num2} is : {num1 + num2}")
    return output

def subtract(num1, num2):
    output = print(f"The subtraction of {num1} and {num2} is : {num1 - num2}")
    return output

def multiply(num1,num2):
    output = print(f"The multiplication of {num1} and {num2} is : {num1 * num2}")
    return output

def divide(num1,num2):
    output = print(f"The division of {num1} and {num2} is : {num1 / num2}")
    return output


def calculation():
    if operation == '+':
        add(num1=num1, num2=num2)
  
    elif operation == '-':
        subtract(num1=num1, num2=num2)
    elif operation == '*':
        multiply(num1=num1, num2=num2)
    elif operation == '/':
        divide(num1=num1, num2=num2)
    else:
        print("Please enter correct operation")


should_continue = True
while should_continue:
    
    num1 = int(input("Enter 1st value :\n >>  "))
    num2 = int(input("Enter 2nd value :\n >>  "))
    operation = str(input("Enter operation to perform '+','-','/','*': \n>>  "))

    
    calculation()

    restart = str(input("\nDo you want to continue 'y', 'n': \n"))

    if restart == 'n':
        should_continue = False
        print("GoodBye")
