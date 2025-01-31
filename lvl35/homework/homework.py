list1 = [3, 7, 12, 5, 9]
list2 = [15, 2, 8, 20, 4]
list3 = [6, 18, 1, 14, 10]

print(max(list1))
print(max(list2))
print(max(list3))

list4 = [11, 23, 45, 2, 9]
list5 = [7, 33, 19, 1, 22]
list6 = [5, 17, 29, 3, 14]

print(min(list4))
print(min(list5))
print(min(list6))

list7 = [4, 8, 15, 16, 23, 42]
list8 = [1, 2, 3, 4, 5, 6, 7]
list9 = [9, 8, 7, 6, 5]

print(len(list7))
print(len(list8))
print(len(list9))

list10 = [2, 4, 6, 8, 10]
list11 = [1, 3, 5, 7, 9]
list12 = [11, 13, 15, 17, 19]

print(sum(list10))
print(sum(list11))
print(sum(list12))

list13 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list14 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list15 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
list16 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print(list13[:4])

for i in range(3, 8):
    print(list14[i])

print(list15[8:5:-1])

i = 0
while i < len(list16):
    print(list16[i])
    i += 1

def analyze_list(lst):
    print(max(lst))
    print(min(lst))
    print(sum(lst))
    print(len(lst))

user_list = [int(x) for x in input().split()]
analyze_list(user_list)
