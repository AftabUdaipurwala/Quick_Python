# Creating first while loop
i = 0
while (i < 10):
    print(i)
    i += 1

# password checker using while loop
correct_password = 'python123'
passwd = input('Enter a Password : ')

while passwd != correct_password:
    print('Your password is incorrect')
    passwd = input('Enter a Password')
print('You are logged in')
