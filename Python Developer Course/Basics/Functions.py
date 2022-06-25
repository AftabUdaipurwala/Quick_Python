# Basic function
# importing date class from datetime module
from datetime import date


# creating the date object of today's date

def age_calc(birthyear):
    todays_date = date.today()
    year = todays_date.year
    age = year - birthyear
    return age  # return the value, the returned value can be reused n number of times


age_calc(1986)
print(type(age_calc(1986)))


# functions without arguements
def printing():
    print("Hello World")  # prints but doesnt return anything, hence the type of this function is none type


printing()
print(type(printing()))


# calculate the length of the string
def stringlencal(strings):
    return len(strings)


stringlencal('Aftab Udaipurwala')


# function with multiple parameters
def converter(original_unit, coeff):
    return original_unit * coeff


print(10, 0.3048)
