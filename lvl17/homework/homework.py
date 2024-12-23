user_age = int(input("Enter your age: "))
friend_age = int(input("Enter your friend's age: "))

if friend_age > user_age:
    print("You are little so be afraid of diddy")
elif user_age > friend_age:
    print("You are safe from diddling")
else:
    print("You and your friend are the same age!")