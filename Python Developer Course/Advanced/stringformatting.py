# password checker using while loop
correct_password = 'python123'
name = input('Enter your name : ')
passwd = input('Enter a Password : ')

while passwd != correct_password:
    print('Your password is incorrect')
    passwd = input('Enter a Password')
print('hi, %s, You are logged in' % name)
message = ('Hi {} whats your plan for the day'.format(name))
print(message)
