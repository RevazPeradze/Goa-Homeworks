def check_number(num):
    if num < 10:
        print("Please enter a larger number.")
    else:
        print("Task complete.")

number = float(input("Enter a number: "))
check_number(number)