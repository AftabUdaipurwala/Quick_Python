# Numbers Section

a = 10  # integer
b = 1.1  # float
c = 1.2 + 5j  # complex
d = 0B1010  # binary
e = 0xFF  # hexadecimal
f = 0o12  # Octal values
print(f)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))  # Hexadecimal values represented as int
print(type(f))  # octal values represented as int
print(hex(10))
print(oct(10))
print(bin(10))

# Strings
# Comment by single line
'''Multi line
comments are written in triple quotes'''

strings = 'Strings are great'
print(strings)
print(len(strings))  # even spaces are considered here
print(strings * 3)  # repetition
print(strings[0:3])  # slicing
print(strings[-4:-1])  # reverse slicing
print(strings[::-1])  # reverse writing of strings
print(strings[::2])  # jump by 2
print(strings[1:6:2])  # slicing and jumping by 2
