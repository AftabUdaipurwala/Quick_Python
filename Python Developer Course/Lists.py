# creating a first list
lst = [1, 2, 3, 4]
lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3, 'A']
lst3 = [lst, lst1, lst2]
print(lst, lst1, lst2, lst3, sep='=====')

# accessing first item of each list
print(lst[0], lst1[0], lst2[0], lst3[0])
print(len(lst))
print(len(lst3[0]))  # see you get 4 here means u have 4 elements in the list which is at 1st index position of the lst3
print(type(lst2[3]))  # see others were integer but the last one is string, so list can hold multiple datatypes

# indexing and slicing
lst2[-1]  # negative indexing
lst2[-3:-1]  # you need to have bigger number on left if you are going by negative indexing

'''Here are more examples of slicing lists if you're still not sure how slicing works.

Let's suppose we have the following list in our Python shell:'''
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[0:3]
days[0:4]
days[:]

# Ranges
list(range(1, 10))
# step function in ranges
list(range(1, 10, 2))  # So, the count happens every two items starting from 1 and ending at 9.
