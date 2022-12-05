



# The meaning of Encapsulation, is to make sure that "sensitive" data is hidden from users. To achieve this, you must:

# declare fields/variables as private
# provide public get and set methods, through properties, to access and update the value of a private field

# Why Encapsulation?
# Better control of class members (reduce the possibility of yourself (or others) to mess up the code)
# Fields can be made read-only (if you only use the get method), or write-only (if you only use the set method)
# Flexible: the programmer can change one part of the code without affecting other parts
# Increased security of data















# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea 
# of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables 
# and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s 
# variable can only be changed by an object’s method. Those types of variables are known as private variables.

# Python program to
# demonstrate protected members

# Creating a base class
class Base:
	def __init__(self):

		# Protected member
		self._a = 2

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling protected member of base class: ",
			self._a)

		# Modify the protected variable:
		self._a = 3
		print("Calling modified protected member outside class: ",
			self._a)


obj1 = Derived()

obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)
