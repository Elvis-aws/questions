# An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with 
# actual values. It’s not an idea anymore, it’s an actual dog, like a dog of breed pug who’s seven years old. You 
# can have many dogs to create many different instances, but without the class as a guide, you would be lost, not 
# knowing what information is required.
# An object consists of : 
# (1) State: It is represented by the attributes of an object. It also reflects the properties of an object.
# (2) Behavior: It is represented by the methods of an object. It also reflects the response of an object to 
# other objects.
# (3) Identity: It gives a unique name to an object and enables one object to interact with other objects.

# Python3 program to
# demonstrate instantiating
# a class


class Dog:
	
	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

# The self
# Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter 
# when we call the method, Python provides it. If we have a method that takes no arguments, then we still have to 
# have one argument. When we call a method of this object as myobject.method(arg1, arg2), this is automatically 
# converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.

# __init__ method
# The __init__ method is similar to constructors in C++ and Java. Constructors are used to initializing the object’s 
# state. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed 
# at the time of Object creation. It runs as soon as an object of a class is instantiated. The method is useful 
# to do any initialization you want to do with your object.

# A Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)

p = Person('Nikhil')
p.say_hi()

# Class and Instance Variables
# Instance variables are for data, unique to each instance and class variables are for attributes and methods 
# shared by all instances of the class. Instance variables are variables whose value is assigned inside a 
# constructor or method with self whereas class variables are variables whose value is assigned in the class.

# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.
	
# Class for Dog
class Dog:

	# Class Variable
	animal = 'dog'			

	# The init method or constructor
	def __init__(self, breed, color):
	
		# Instance Variable	
		self.breed = breed
		self.color = color	
	
# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)	



# Python3 program to show that we can create
# instance variables inside methods
	
# Class for Dog
class Dog:
	
	# Class Variable
	animal = 'dog'	
	
	# The init method or constructor
	def __init__(self, breed):
		
		# Instance Variable
		self.breed = breed			

	# Adds an instance variable
	def setColor(self, color):
		self.color = color
	
	# Retrieves instance variable	
	def getColor(self):	
		return self.color

# Driver Code
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
