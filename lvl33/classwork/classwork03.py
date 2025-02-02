numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

min_number = numbers[0]

for i in range(len(numbers)):
    if numbers[i] < min_number:
        min_number = numbers[i]

       
print(min_number)


print(len(numbers))