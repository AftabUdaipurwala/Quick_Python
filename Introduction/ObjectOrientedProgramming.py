class Person:
    def __init__(self,age,add):
        self.age = age
        self.add = add

    def getaddress(self):
        return self.add[:3]
    def getadults(self):
        if self.age>18:
            return "Adult"


p = Person(32,'Mumbai')
out = p.getadults()
print(out)
out = p.getaddress()
print(out)