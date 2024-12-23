def calculate_bmi(weight, height):
    """
    Calculate BMI and return the category.
    """
    try:
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        return f"BMI: {bmi:.2f} ({category})"
    except:
        return "Invalid input."

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

print(calculate_bmi(weight, height))