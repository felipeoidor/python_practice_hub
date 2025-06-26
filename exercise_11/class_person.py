# Define a class named Person 
class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Define method "greet"
    def greet(self):
        print(f"Hello, my name is {self.name}")

# Create an instance of the person class
first_person = Person("Pipe", 31)
first_person.greet()