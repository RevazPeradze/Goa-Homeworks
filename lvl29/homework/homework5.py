from datetime import datetime

def agecalc(age):
    current_year = datetime.now().year
    birth_year = current_year - age
    print(f"If you are {age} years old, you were born in {birth_year}.")
