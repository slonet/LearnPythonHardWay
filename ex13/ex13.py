from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is", third)

# 1st variable passed from argv is the name of the python file running
# subsequent variables are collected from the terminal arguments entered when the script was run
