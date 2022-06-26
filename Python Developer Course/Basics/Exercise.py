'''Functions, Conditionals, and Loops (E)
Take a look at the following function:

def cel_to_fahr(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
The function gets Celsius degrees as input and converts them to Fahrenheit.

Implement a for loop that iterates through the list temperatures = [10, -20, 100] and call the above cel_to_fahr function in each iteration.

In other words, this time you are using the function to calculate a series of values instead of just one value'''


def cel_to_fahr(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


temperatures = [10, -20, 100]
for i in temperatures:
    print(cel_to_fahr(i))
