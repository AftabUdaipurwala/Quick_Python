import datetime

# Using % for indicating placeholders , %s for string, %f for float and %i for int etc
name = 'Aftab'
age = 30.3
date=str(datetime.date.today())
print('Todays date is %s , my name is %s and my age is %.2f'%(date,name,age))

# Alternativeliy u can also use the format syntax inside print statement
name,age, profession = 'Aftab Udaipurwala', 30.3,'Python Developer'
print("Name is {0}, age is {1} and profession is {2}" .format(name, age, profession))
