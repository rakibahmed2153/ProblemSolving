class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name is : {self.name}, Age is: {self.age}")    
    def behaiveour(self):
        print("I can't do anything")

class cat(animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def behaiveour(self):
        print("Meow")    

class dog(animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def behaiveour(self):
        print("Bark") 
    def show(self):
        print(f"Name is : {self.name}, Age is: {self.age}, color is: {self.color}")      

firstAnimal = animal('Animal', 50)
firstAnimal.show() 
firstAnimal.behaiveour() 

secondAnimal = dog('Dog', 90, 'red')
secondAnimal.show() 
secondAnimal.behaiveour() 

