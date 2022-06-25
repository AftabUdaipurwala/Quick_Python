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


# Functions wiht Default parameters

def converter(original_unit, coeff=0.20):
    return original_unit * coeff


# dont pass default parameters
print(converter(10))
print(converter(10, 0.3))

# Weather Function (E)
'''Create a function that converts Celsius degrees to Fahrenheit. 
The formula to convert Celsius to Fahrenheit is F = C × 9/5 + 32.
This is not an interactive exercise. 
Write this function using Python like you normally do'''


def weather(Celsius):
    F = (Celsius * 9 / 5) + 32
    return F


print(weather(36.2))

# Functions and If else
'''In one of the previous exercises, we created this function:
def string_length(mystring):    
    return len(mystring)
Calling the function with a string as the value for the argument mystring will return the length of that string.
If an integer is passed as an argument value:
string_length(10)
that would generate an error since the len() function doesn't work for integers.
Your duty is to modify the function so that when an integer is passed as input, the function should output a message like "Sorry integers don't have length."'''


def lenofstr(string):
    if type(string) == int:
        return 'Sorry integers don\'t have length.'
    elif type(string) != str:
        return 'Sorry not a valid string type'
    else:
        return len(string)


lenofstr('Aftab')
