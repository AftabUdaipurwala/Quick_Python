# under normal condition
a = int(input('Enter a number'))
b = int(input('Enter a number'))

if a > b:
    print('A is greater than B')
else:
    print('B is greater than A')

# when u have many if elses
a = int(input('Enter a number'))
b = int(input('Enter a number'))

if a > b:
    print('A is greater than B')
elif a == b:
    print('A is equal to B')
else:
    print('B is greater than A')
