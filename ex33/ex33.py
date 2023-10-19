def make_numbers(n, step):
	i = 0
	numbers = list(range(0, n, step))

	print("The numbers: ")

	for num in numbers:
		print(num)

make_numbers(10, 2)