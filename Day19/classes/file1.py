class Person:
      
     #Constructor

     def __init__(self,id,name,loc1):
          self.id=id
          self.name=name
          self.loc1=loc1
    
     def display(self):
          print( self.id,"-",self.name,"-",self.loc1)

#Object
person=Person(101,"Nageswara","India")
person.display()
print(id(person))
print(type(person))

print(type(100))
print(type(100.00))
print(type("100"))
print(type(True))
print(type(10+5j))