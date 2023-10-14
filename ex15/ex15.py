from sys import argv

# read in command line argument for file name
script, filename = argv

# read the contents of the file into the txt variable
txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())

print("Type the filename again:")
# get the same file name information from a terminal prompt instead of an argument
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
# close the files when you're done using them
txt.close()
txt_again.close()