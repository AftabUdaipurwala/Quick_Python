dict1 = {'Nike': 'Shoes', 'HP': "Computer", 'Mahindra': "Tractor"}
dict1['Mahindra']
dict1['Nike']
dict1['HP']
# adding
dict1['Tupperware'] = 'Bottles'
print(dict1)
# removing
del dict1['Nike']
print(dict1)

dict1.pop('Mahindra')
print(dict1)

# Mapping two lists to a dictionary:
keys = ["a", "b", "c"]
values = [1, 2, 3]
mydict = dict(zip(keys, values))
mydict
