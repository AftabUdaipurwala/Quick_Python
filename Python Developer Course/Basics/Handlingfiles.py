myfile = open(
    'E:\\WorkStation Laptop\\Learning Material\\Python Learning\\Quick Python\\Python Developer Course\\Basics\\sample.txt')
fruits = myfile.read()  # read the data of a file in another variable
myfile.close()  # close file after use
fruits = fruits.splitlines()
for i in fruits:
    print(i)

# checking the file type which is __io.TextIOWrapper
type(myfile)
# now if you read again , it shows only '' because its cursor goes to the end of the file
myfile.read()
# to bring back the cursor to the start of the text file do
myfile.seek(0)
# now read again,
myfile.read()

# reading contents
"Hello \n World".splitlines()

"banana" in ['banana', 'apple', 'orange']

'''Download the text file from the attachment.
Then, write some code that reads the content of the file and generates the output'''

myfile = open(
    'E:\\WorkStation Laptop\\Learning Material\\Python Learning\\Quick Python\\Python Developer Course\\Basics\\fruits.txt')
fruits = myfile.read()
print(fruits)
myfile.close()
