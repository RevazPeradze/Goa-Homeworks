secret_password = "aint no party like p diddys party"

guess = ""

while guess != secret_password:
    guess = input("Guess the password: ")
    
    if guess == secret_password:
        print("Congratulations! You've guessed the password and won!")
    else:
        print("Wrong password, try again!")