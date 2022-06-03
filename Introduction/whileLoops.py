# While loop will work till the condition is false
c =0
while c<5:
    print(c)
    c+=1

# using break condition
c=0
while c<5:
    print(c)
    c+=1
    if c%3==0:
        break
# using continue statement
c=0
while c<=5:
    if c==3:
        c+=1
        continue
    print(c)
    c+=1

# pass statement is a filler statement, it doesnt do anything but is used when u are not sure what u want to write
c=0
if c==0:
    pass