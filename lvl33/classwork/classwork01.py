def func(name):
    name = name[::-1]
    for i in name:
        print(i)
    
print(func(input('enter your name: ')))