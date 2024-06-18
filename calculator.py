def calculator(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    else:
        return "Invalid Operation"
    
print("****  WELCOME  ****")
while True:
    
    option = input("do you want to continue (y/n) : ").lower()
    if option in ["y","n"]:
        if option == "y":
            try :
                num1 = int(input("Enter the first number :"))
                num2 = int(input("Enter the second number :"))
                operation = input("Enter the operation from (add/sub/multiply/divide) :").lower()
                if operation in ["add", "sub", "multiply", "divide"]:
                    result = calculator(operation,num1,num2)
                    print(f"The result is {result}")
                else:
                    print("operaton should be from (add/sub/multiply/divide)")
            except ValueError:
                print("num should have base 10")
        else:
            break
    else:
        print("please enter a valid option either y or n")
           
print("****  THANK YOU  ****")
    
