# Python calculator

operator = input('Emter an operator (+ - * /): ')
num1 = float(input('Enter the 1st number: '))
num2 = float(input('Enter the 2md number: '))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"{operator} is not a valid option")



