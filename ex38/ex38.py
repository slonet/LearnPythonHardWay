ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
				"Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("Adding: ", next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

# returns the 2nd items in the list
print(stuff[1])
# returns the last item in the list
print(stuff[-1]) # woah! fancy
# returns the last item in the list (or whichever is specified) and removes it from the list
print(stuff.pop())
# joins the items in the list with the specified string between them
# the join function is applied to the string that you want to use as the joiner
print(' '.join(stuff)) # what? cool!
# joining specific elements in the list
print('#'.join(stuff[3:5])) # super stellar!