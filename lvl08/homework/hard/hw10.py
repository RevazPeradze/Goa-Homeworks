user_age = int(input("Enter your age: "))

dad_age = int(input("Enter your dad's age: "))

user_age_in_15_years = user_age + 15
dad_age_in_15_years = dad_age + 15

age_ratio_in_15_years = dad_age_in_15_years / user_age_in_15_years


print(f"In 15 years, your dad will be {age_ratio_in_15_years:.2f} times older than you.")