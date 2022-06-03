list1 = [1,2,3,4,5,6]
print(list1)
fruits =['Bananas','Apples','Oranges','Mangoes']
print(fruits)  #print entire list
print(fruits[0]) # get the first item in fruits list
print(fruits[3]) # get the Mangoes which are at the 4th
print(fruits[2]) # get the 3rd item in the list
print(list1[3:])

# add items to the list
fruits.append('Blueberries')
print(fruits)
# replace/update values :  apples to cherries
fruits[1] ='Cherries'
print(fruits)
# remove items from the list
del fruits[0]
print(fruits)

# Arithmatic operations in array
print(len(fruits)) # get the lenght of the list
print(list1*3) # repeat list 3 times
print(list1+fruits) # add 2 lists
print(max(list1)) # get the max of list
print(min(list1)) # get the min of list
