# Classes represent some entity
# Class to represent vehicles

# class names should be UppperCamelCase

# the more generic class is called the "parent" class
class Vehicle:
    '''docstring'''
    # declare a variable inside of the class
    # This variable will be put on every object that gets created
    wheels = 4

    # Constructor (allows us to provide data to the class before it "constructs" the object)
    # these variables will now be required in order to create a Vehicl Object
    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.year = int(year)  
        self.mileage = int(mileage)
        self.color = color

    def honk(self):
        '''docstring'''
        print("HOOOONK!")

# the more specific class is called "child" class
# The child class inherits from the parent class
class Car(Vehicle):
    '''docstring'''
    # If i want to add additional attributes to a child class, I still need to include
    # all of the attributes from parent class, but I don't have to list them out.
    def __init__(self, make, model, color, year, mileage, style):
        super().__init__(make, model, color, year, mileage)
        # and adds on style as one additional attribute
        self.style = style

    def description(self):
        '''docstring'''
        print("I am a", self.make, self.model, "with", self.mileage,
              'miles. I am a', self.color, self.style + '.')

    def drive(self, miles_driven):
        '''docstring'''
        self.mileage = self.mileage + miles_driven

    # the @staticmethod decorator allows us to invoke the method without pass in 'self"
    # the @property decorator allows us to invoke a function without trailing parentheses.
    @staticmethod
    def lock_doors():
        print('doors are locked!')


# If I include code here at teh bottom for testing or debugging
# This code will get run whenever the module gets imported
# IF I don't want this code to run when file is imported as a module
# but I *DO* want it to run when it's executed as a script.
# I can put it inside of this fancy if statement
if __name__ == "__main__":
    my_car = Car('Toyota', 'Camry', 'gray', 2007, 248000, 'sedan')

    print(my_car.style)
    print(my_car.drive(6000))
    print(my_car.mileage)




    