class Car(object): # Use 'object' so that class inherits the OBJECT class.
  condition = 'new' # Member variable
  def __init__(self, model, color, mpg):
      self.model = model
      self.color = color
      self.mpg = mpg
  def display_car(self):
      print "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

  def drive_car(self):
      my_car.condition = 'used'

class ElectricCar(Car):
  def __init__(self, model, color, mpg, battery_type):
    super(ElectricCar, self).__init__(model, color, mpg) # using SUPER keyword to inherit __init__ attributes from original Car class.
    self.battery_type = battery_type

my_car = Car("Tercel", "red", 88) # Do not need to include SELF keyword when creating instance of a class.
print my_car.condition
print my_car.display_car()

class Animal(object): # User-created classes always begin with a capital letter.
    is_alive = True # This is referred to as SCOPE. Not all variables are available at all times. Available everywhere (GLOBAL vars),
                   # only available to certain class (MEMBER vars), only available to a certan instance of a class (INSTANCE vars).
                   # is_alive is a MEMBER variable, while age is an INSTANCE variable.
                   # The same applies to functions - global, member, instance.
    health = 'good'
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
    def description(self): # You can create methods for classes. __init__ is a method, but so is this one, 'description'.
        print self.name, "is my name."
        print "I am", self.age, "years old."

zebra = Animal("Jeffrey", 2, False)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)
hippo = Animal("Geronimo", 3, True)
sloth = Animal("Jim", 12, False)
ocelot = Animal("Jenny", 1, True)

print sloth.health
print ocelot.health
print hippo.health

hippo.description()   # Calling the description method.

print zebra.name, zebra.age, zebra.is_hungry, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_hungry, giraffe.is_alive
print panda.name, panda.age, panda.is_hungry, panda.is_alive

# INHERITANCE and MORE ADVANCED CLASS TOPICS

# Syntax for Inheritance -- class DerivedClass(BaseClass)
# Derived classes are also called SUBCLASS. Base classes are called PARENT or SUPERCLASS

class Shape(object):
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape): # Triangle inherits from Shape class
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

# Overriding class metbods while inheriting

class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print "Hello %s." % other.name
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class CEO(Employee): # CEO inheriting from the Employee class
    def greet(self, other): # CEO overriding the greet method
        print "Get back to work, %s!" % other.name

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours) # SUPER directly accesses attributes/methods of PARENT class

ceo = CEO("Emily")
emp = Employee("Dave")
milton = PartTimeEmployee("Milton")


emp.greet(emp)
ceo.greet(emp)
print milton.full_time_wage(10)