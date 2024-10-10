class Animal:

    #Constructor(initializer)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Instance Method
    def get_age(self):
        return f"{self.name} is {self.age} years old"



class Dog(Animal):  # ()----> Inheritance of Animal class
    #Local class attribute 
    species = 'Canis Famillaris'

    #Instance Method
    def bark(self):
        return f"{self.name} says woof!!"



class Cat(Animal):  # ()----> Inheritance of Animal class
    #Local class attribute 
    species = 'RagDol'

    #Instance Method
    def mew(self):
        return f"{self.name} says Meow!!"

    
    
#Object of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

#Object of the Cat class
cat1 = Cat("Buddy", 3)
cat2 = Cat("Charlie", 5)

#Accessing attributes & methods
print(dog1.bark())
print(dog2.get_age())
print(dog1.species)
print("\n")
print(cat1.mew())
print(cat2.get_age())
print(cat1.species)