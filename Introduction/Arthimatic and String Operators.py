# Arithmatic operation
a = 13
b= 12
print(a+b) # summation
print(a-b) # difference
print(a*b) # multiplication
print(a/b) # division
print(a//b) # integer division
print(a%b) # modulo division, getting remainder

# String operations
sent1 = 'Mumbai is a city'
fname ='Aftab'
lname = 'Udaipurwala'
print(fname+' '+lname) # here we know that + sign is overloaded to have multiple work to be done, eg adding and concatenating
print(fname*3) # repeat multiple times

# Indexing strings
print(sent1[0:8]) # get everything from 1st till 7th character
print(sent1[1:8])# get everything from 2nd till 7th character
print(sent1[:8]) # get everything till 7th character
print(sent1[0:8:2]) # jump by 2 steps