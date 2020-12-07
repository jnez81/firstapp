# Class methods

class Person:  
    number_of_people = 0  # class attribute

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod # decorator
    def number_of_people_(cls):  # class method
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("James")
p2 = Person("Jackie")
print(Person.number_of_people_())