dict1 = {'Mike': 123, "john": 345, 'Nick': 678}
lst1 = [1, 2, 3, 45, 6]

for i in lst1:
    print(i)

for keys in dict1.keys():
    print(keys)

for values in dict1.values():
    print(values)

# perform operation in the loop
a = []
for i in lst1:
    c = i + 10
    a.append(c)
print(a)

# iterate through the file
myfile = open(
    'E:\\WorkStation Laptop\\Learning Material\\Python Learning\\Quick Python\\Python Developer Course\\Basics\\fruits.txt')
c = myfile.read()
myfile.close()
a = c.splitlines()
for i in a:
    print('Fruit is :', i)

mylist = ["Terribly Tricky"]
for word in mylist:
    for letter in word[-6:]:
        print(letter)

# Create a for loop that iterates through all the items of the following list and prints the item if the item is greater than 2.

mylist = [1, 2, 3, 4, 5]
for i in mylist:
    if i > 2:
        print(i)

# write some code that prints (inserts) the length of each string in the fruits.txt file.

myfile = open(
    'E:\\WorkStation Laptop\\Learning Material\\Python Learning\\Quick Python\\Python Developer Course\\Basics\\fruits.txt')
c = myfile.read()
myfile.close()
a = c.splitlines()
for i in a:
    print(len(i))
