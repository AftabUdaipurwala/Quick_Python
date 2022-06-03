# if else conditional statement

x = int(input('Give your 1st input as integer '))
y= int(input('Give your 2nd input as integer '))

if (x>y):
    print('1st number greater than 2nd')
elif (x==y):
    print('1st and 2nd number are equal')
else:
    print('2nd number is greater than 1st number')

# use of and , or , nor
age = int(input('Enter age'))
if (age>0 and age <3):
    print('Infants')
elif (age>3 and age <13):
    print('Children')
elif (age >13 and age<18):
    print('Teenagers')
elif (age>60 and age<200 ):
    print('Senior Citizen')
else:
    print('Adult')