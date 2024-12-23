string = "IDKWHAT"
print(string[1])

num1 = 10
num2 = 20
print(num1 + num2)

str1 = "Hello"
str2 = "World"
print(str1 + str2)

a = 10
b = 3
print(a / b)

print(5 > 3)
print(4 < 2)
print(6 >= 6)
print(5 <= 7)
print(8 == 8)
print(9 != 10)

print(5 + 5 == 8 + 2)
print((5 > 3) and (4 < 6))
print((6 > 7) or (2 < 3))
print(not (5 == 6))

for i in range(1, 11):
    print(i)

nums = [1, 2, 3, 4, 5]
total = 0
for n in nums:
    total += n
print(total)

for char in "Hello, World!":
    print(char)

i = 1
while i <= 10:
    print(i)
    i += 1

i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1

i = 1
sum = 0
while sum < 50:
    sum += i
    i += 1
print(sum)