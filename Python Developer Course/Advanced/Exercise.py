'''Merging Text Files (E)
Here is another tricky exercise.
1. Download and put into a folder the three text files attached in this lecture. The first text file contains the text Content1 ; the second file contains Content2 ; and the third file contains Content3 .
2. You should create a Python script that generates a new text file, which should contain the content of all three text files. The generated file should have this content:
Content1
Content2
Content3
In other words, your Python script should merge the three text files.
3. The name of the output file should be the current timestamp. Example: 2017-11-01-13-57-39-170965.txt
'''
import datetime
import os

lst1 = os.listdir()
# Import re module to use regular expression
import re

# Declare the list contains subject code
sublist = ['CSE-407', 'PHY-101', 'CSE-101', 'ENG-102', 'MAT-202']


# Declare the filter function
def Filter(datalist):
    # Search data based on regular expression in the list
    return [val for val in datalist
            if re.search(r'file', val)]


# Print the filter data
print(Filter(lst1))
lst2 = Filter(lst1)
for i in lst2:
    val = i
    with open(i, 'a') as myfile:
        contents: str = myfile.read()
        with open('temp.txt', 'a') as mywritefile:
            mywritefile.write(contents)

timestamp = datetime.datetime.now()
dated = timestamp.strftime('%Y-%m-%d %H-%m')
dated = str(dated) + '.txt'
with open('temp.txt', 'r') as myfilewritten:
    contents2 = myfilewritten.read()
    with open(dated, 'w') as writtenfinal:
        writtenfinal.write(contents2)
