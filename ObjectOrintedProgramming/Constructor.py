# A constructor is a special method that is used to initialize objects. The advantage of a constructor, is that 
# it is called when an object of a class is created. It can be used to set initial values for fields:
#  In Python the __init__() method is called the constructor and is always called when an object is created.

class GeekforGeeks:

	# default constructor
	def __init__(self):
		self.geek = "GeekforGeeks"

	# a method for printing data members
	def print_Geek(self):
		print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()
