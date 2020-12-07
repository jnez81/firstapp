# Object Oriented Programming Examples

class Dog:
    def __init__(self, name, age, color): 
        self.name = name
        self.age = age
        self.color = color 

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_color(self):
        return self.color

    def set_age(self, age):
        self.age = age

d = Dog("James", 39, "brown")
print(d.get_name())
print(d.get_age())
print(d.get_color())

