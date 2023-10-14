# placing end = ' ' at the end of a string changes the default end character (usually \n)
print("How old are you?", end = ' ')
# the input() function grabs text input from the terminal. The text input is automatically formated as a string
# special characters are automatically escaped
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")