class Laptop():

	# the init method can receive arguments. In this case, they are stored directly as variables.
	def __init__(self, owner, ram_capacity, ram_type, ram_speed, cpu_type, cpu_cores, 
				cpu_freq, storage_capacity, storage_type):
		self.owner = owner
		self.ram_capacity = ram_capacity
		self.ram_type = ram_type
		self.ram_speed = ram_speed
		self.cpu_type = cpu_type
		self.cpu_cores = cpu_cores
		self.cpu_freq = cpu_freq
		self.storage_capacity = storage_capacity
		self.storage_type = storage_type

	def describe(self):
		print(f"{self.owner}'s laptop has an {self.cpu_cores} core {self.cpu_type} processor")
		print(f"It has {self.ram_capacity} of {self.ram_speed} {self.ram_type} RAM")
		print(f"It also has a {self.storage_capacity} {self.storage_type}")


mom_laptop = Laptop('Nan', '16 GB', 'DDR4', '1.4 GHz', 'Intel Core i7', '8', '3.0 GHz', '128 GB', 'HDD')
# the variables declared in the __init__ method can be accessed by 'object.variable'. NOT 'object.variable()'
# since these are not methods

mom_laptop.describe()

print("Let's upgrade the storage.")
print("Enter a new storage type")
mom_laptop.storage_type = input("> ")

print("Enter a new storage capacity")
mom_laptop.storage_capacity = input("> ")

print("Now here's the new laptop.")

mom_laptop.describe()


tyler_laptop = Laptop('Tyler', '32 GB', 'DDR5', '2.0 GHz', 'AMD Ryzen', '10', '3.1 GHz', '512 GB', 'SSD')

print("\n", "-" * 20, "\n")
tyler_laptop.describe()