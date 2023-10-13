# create int variable and set it to 10
types_of_people = 10
# formatted string using the above variable
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# formatted string using two variables
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
# formatted strins using variables inside of print functions
print(f"I said: {x}")
print(f"I also said: '{y}'")
# assign boolean value to this variable
hilarious = False
# string with an empty parameter "curly braces"
joke_evaluation = "Isn't that joke so funny?! {}"
# .format inserts a variable into the empty parameter in the string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# concatenate two strings in a print function
print(w + e)