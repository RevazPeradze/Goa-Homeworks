def add_five():
    try:
        user_input = int(input("Please enter a number: "))
        result = user_input + 5
        print(f"The number that is 5 greater than {user_input} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

add_five()