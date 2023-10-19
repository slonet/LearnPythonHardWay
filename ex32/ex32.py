the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of loop goes through a list
for number in the_count:
	print(f"This is the count {number}")

# same as above
for fruit in fruits:
	print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
for i in change:
	print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# range(start, stop, step) creates an incrementing range including the 1st element and < the last element
# you can run range with one argument to just define the stop value. it will start at 0 an increment
# by one in this case
for i in range(0, 6):
	print(f"Adding {i} to the list.")
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
# for will iterate over the elements inside of the list
for i in elements:
	print(f"Element was: {i}")