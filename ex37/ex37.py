from sys import argv
from sys import exit

script, n, limit = argv

try:
	n = int(n)
	limit = int(limit)
except:
	print(f"Both arguments must be integers.")
	exit(1)


def continue_test(n, limit):
	for i in range(n):
		if i < limit:
			print(f"The index is {i}")
		else:
			print("The index got too large so I stopped printing it.")
			continue

lambda_test = lambda a, b: a + b ** (1/a)

def nop():
	pass
	print("Do you do things after the pass?")


def print_file(file_path):
	with open(file_path, 'r') as file:
		print(file.read())

def yield_test(n):
	for i in range(n):
		yield i/n
		i += 1


# continue_test(n, limit)
#print(lambda_test(n, limit))
#nop()
#print_file("ex37.txt")
x = yield_test(n)
print(next(x))