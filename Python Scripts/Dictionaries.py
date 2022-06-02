studentrecord = {'Aftab': 30, 'Ajay':23,'Sameer':20}

# get ages of Ajay and Sameer by accessing its key
print(studentrecord['Sameer'])
print(studentrecord['Ajay'])

# delete record of Aftab
del studentrecord['Aftab']
print(studentrecord)

# never create dictionaries like this
studentrecord = {'Aftab': 30, 'Aftab':23,'Aftab':20}
