num1 = float(input("input first numbrr "))
num2 = float(input("input second number "))
operator = input("input operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
    print(f"resultati {num1} + {num2} is: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"resultati {num1} - {num2} is: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"resultati {num1} * {num2} is: {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"resultati {num1} / {num2} is: {result}")
    else:
        print("nolze ver gaiyofa")
else:
    print("arasworia sheiyvane operatori mag: +, -, *, /.")