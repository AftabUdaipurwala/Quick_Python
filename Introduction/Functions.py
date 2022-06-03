def average(num1,num2):
    try:
        result = num1/num2
        return result
    except:
        result ='Invalid numbers'
        return result

x = int(input('Enter 1st number '))
y = int(input('Enter 2nd number '))
out = average(x,y)
print(out)