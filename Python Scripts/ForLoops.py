# using for loops with list
list1= ['Apple','Banana','cherries','mangos']
for i in list1:
    print(i)

# using for loops with tuples
t = (1,2,3,4,5)
for i in t:
    print(i)

# using for loops with range
for i in range(1,10,2): # skip the even numbers from 1 to 10
    print(i)

# get first 10 multiples of 5
for i in range(1,51):
    if i%5==0:
        print(i)