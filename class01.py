class person():
	def __init__(self, name): 
		# 參數名稱self是慣例,可任意改
		# self represents the instance of the class.
		self.name = name

'''
class person():
	def __init__(self, x):
		self.name = x 
'''
# 同上

class MDperson(person):
	def __init__(self, name):
		self.name = "Doctor " + name

class JDperson(person):
	def __init__(self, name):
		self.name = name + ", Esquire"


hunter = person("Joe")
print(hunter.name)


class car():
	def exclaim(self): # self物件
		print("I'm a car!")
	def power(self):
		print("I need some oil!")


class Honda(car):
	def exclaim(self):
		print("I'm a Honda! Much like a Car, but more Honda-ish.")
	def need_a_push(self):
		print("A little help here?")

aCar = car()
aHonda = Honda()

aCar.exclaim() 
aHonda.power()
# car.exclaim(aCar)
# car().exclaim()

aHonda.exclaim()

aPerson = person("Kobe")
doctor = MDperson("Kobe")
lawyer = JDperson("Kobe")
print(aPerson.name, doctor.name, lawyer.name, sep = "\n")

aHonda.need_a_push()

class Emailperson(person):
	def __init__(self, name, email):
		super().__init__(name)
		# person.__init__(self, name) 
		# super() is a temporary object of the superclass
		self.email = email


joe = Emailperson("Joe Johnson", "handsome@gmail.com")
print("Name:", joe.name, "\nEmail:", joe.email)