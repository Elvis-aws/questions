# The @classmethod decorator is a built-in function decorator that is an expression that gets evaluated after 
# your function is defined. The result of that evaluation shadows your function definition. A class method receives 
# the class as an implicit first argument, just like an instance method receives the instance 

# A static method does not receive an implicit first argument. A static method is also a method that is bound to 
# the class and not the object of the class. This method can’t access or modify the class state. It is present 
# in a class because it makes sense for the method to be present in class.

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a class method to create a Person object by birth year.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
