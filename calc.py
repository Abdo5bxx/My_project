from math import *
calculator = True
while calculator == True:
    fir_num = float(input("Enter the first Number: "))
    op = input("Enter the operator (+, -, *, /, ^,sqrt): ")
    sec_num = float(input("Enter the second number: "))
    
    i = 0
    while i < 1:
        i = i + 1
        if op == "+":
            result = fir_num + sec_num
            print(result)
        elif op == "-":
            result = fir_num - sec_num
            print(result)
        elif op == "*":
            result = fir_num * sec_num
            print(result)
        elif op == "/":
            result = fir_num / sec_num
            print(result)
        elif op == "^":
            result = pow(fir_num, sec_num)
            print(result)
        exit = input("Do you want to exit the program (y/n): ")
        if exit == "y":
            calculator = False
        else:
            calculator = True
    