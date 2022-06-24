'''There's another datatype in Python called a tuple :

mytuple = (1, 2, "Three")

It's exactly like a list except:

1. You use parenthesis instead of square brackets to define the tuple.

2. A tuple is not mutable which means you can't append or remove items from tuples, like you can with lists. Trying add an append method to a tuple would throw an error:

Tuples are rarely used. However, if you ever need a list that you really don't want to be changed, using a tuple instead of a list is a good idea.'''

mytuple = (1, 2, 3, 'Aftab')
len(mytuple)
mytuple[0]
mytuple[0:1]
mytuple2 = 9,
print(type(mytuple2))  # means the () are optional for a tuple just specifying a , is enough
