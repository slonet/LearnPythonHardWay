## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## a Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## a dog has-a name
		self.name = name

## a Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## a Cat has a name
		self.name = name

## a Person is-a object
class Person(object):

	def __init__(self, name):
		## a Person has-a name
		self.name = name

		## Person has a pet of some kind (default value for pet is None)
		self.pet = None

## an Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? what is this strange magic?
		## I think this calls the __init__ function of the class being inherited from (parent class)
		super(Employee, self).__init__(name)
		## an Employee has-a salary
		self.salary = salary

## a Fish is-a object
class Fish(object):
	pass

## a Salmon is-a Fish
class Salmon(Fish):
	pass

## a Halibut is-a Fish
class Halibut(Fish):
	pass

## Create a Dog object called rover with the name "Rover"
rover = Dog("Rover")

## Create a Cat object called satan with the name "Satan"
satan = Cat("Satan")

## Create a Person object called mary with the name "Mary"
mary = Person("Mary")

## Assign the pet parameter of mary to be the Cat object satan
## Now calling mary.pet() should return the cat object satan
mary.pet = satan

## create an Employee object called frank with the name "Frank" and the salary 120000
frank = Employee("Frank", 120000)

## assign the pet parameter of the frank object to the Dog object called rover
frank.pet = rover

## create a Fish object called flipper
flipper = Fish()

## create a Salmon object called crouse
crouse = Salmon()

## create a Halibut object called harry
harry = Halibut()