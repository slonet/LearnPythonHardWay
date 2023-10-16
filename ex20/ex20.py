from sys import argv

script, input_file = argv

# reads the whole file
def print_all(f):
	print(f.read())

# sets the line pointer back to the beginning of the file
def rewind(f):
	f.seek(0)

# prints an arbitrary number that happens to be synchronized with the line outside this function
# also prints a line from the file object f
def print_a_line(line_count, f):
	print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# the file object wrapper keeps track of which line has been read last and reads in sequential order
# each line read, increments the line counter internally
current_line = 1
print_a_line(current_line, current_file)

# += 1 is equivelent to var = var + 1
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)