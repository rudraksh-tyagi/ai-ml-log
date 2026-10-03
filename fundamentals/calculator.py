x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = input("Enter an operator (+, -, *, /): ")
if(z == "+"):
    print(x + y)  
elif(z == "-"):
    print(x - y)
elif(z == "*"):
    print(x * y)
elif(z == "/"):
    if y != 0:
        print(x / y)
    else:
        print("Error: Division by zero is not allowed.")
