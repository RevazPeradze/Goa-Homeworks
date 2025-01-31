a, b, c, d = 10, 20, 30, 40

if a < b and c < d:
    print("Both conditions are True")

if a > b or c < d:
    print("At least one condition is True")

if a == 10 and b == 20:
    print("Exact match for both variables")

if b != 25 or d == 40:
    print("One of the conditions is True")

if a < b and not (c > d):
    print("Both conditions hold after negation")

if a > 5 and b > 10:
    print("Values are greater than threshold")

if c == 30 or d == 50:
    print("One value is expected")

if a < b and c >= 30:
    print("Conditions involving greater and equals work")
