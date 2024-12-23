def check_grade(grade):
    if grade >= 50:
        print("You passed!")
    else:
        print("You failed!")

grade = float(input("Enter your grade (0-100): "))
if 0 <= grade <= 100:
    check_grade(grade)
else:
    print("Please enter a valid grade between 0 and 100.")