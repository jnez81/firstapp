class Pet:   # Super class 'Pet'
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

class Cat(Pet):  # Subclass 'Cat'

    def __init__(self, name, age, color):  # Inheriting init method from super class, adding color argument
        super().__init__(name, age)
        self.color = color 
 
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I'm {self.color}")

class Dog(Pet):  # Subclass 'Dog'
    def speak(self):
        print("Bark")

p =  Pet("Channy", 7)
p.show()
c = Cat("Bill", 34, "purple")
c.speak()
d = Dog("Jill", 22)
d.show()
