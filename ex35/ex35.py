from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = input("> ")
	# the in operator is used to see if something is present inside an iterable. 
	# Can be used on any iterable
	if "0" in choice or "1" in choice:
		# casts input to an int which is not guaranteed to work. A try catch block might help.
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		# Not sure what exit() does yet
		exit(0)
	else:
		dead("You greedy bastard!")


def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False

	while True:
		choice = input("> ")

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")

def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")

	choice = input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()


def dead(why):
	print(why, "Good job!")
	# exit() raises the SystemExit exception which causes the interpreter to halt execution
	# commonly used to stop a python program. the exit status 0 indicates successful termination
	exit(0)


def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	choice = input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until your starve.")


start()