def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def flo(a,b):
    return a//b\
    
    operation = input("enter the operator:")
    num1 = int(input("enter the number:"))
    num2 = int(input("enter the number:"))

    if operation == "+":
        print(add(num1,num2))

    elif operation == "-":
        print(sub(num1,num2))

    elif operation == "*":
        print(mul(num1,num2))

    elif operation == "/":
        print(div(num1,num2))

    elif operation == "//":
        print(flo(num1,num2))

    else:
        print("invalid operation") 

    

