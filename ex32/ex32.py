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

# this for loop can be eliminated by creating a list directly fom the range
# elements = list(range(6))

# now we can print them out too
# for will iterate over the elements inside of the list
for i in elements:
	print(f"Element was: {i}")

""" Other list methods:
append()	- adds an element to the end of the list
clear()		- removes all elements from the list
copy()		- returns a copy of the list
count()		- returns the number of elements with the specified value
extend()	- adds the elements of a list to the end of the current list
index()		- returns the index of the 1st element with the specified value
insert()	- adds and element at the specified position
pop()		- removes the element at the specified position
remove()	- removes the 1st item with the specified value
reverse()	- reverses the order of the list
sort()		- sorts the list
"""