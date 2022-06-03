#  Tuples are immutable lists
t1 = ('oranges','apples','bananas')

# cant update a tuple
#t1[0]='cherries'

# we can access the values
print(t1[0])
print(t1[2])

# we can do slicing as lists too
print(t1[:2])

# we can create a new tuple by adding 2 tuples
t2=(1,2,3,4)
t=t1+t2
print(t)

# u can repeat tuples
print(t*3)