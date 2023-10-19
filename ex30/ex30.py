people = 30
cars = 40
trucks = 15

# if performs the 1st logical test. if it is true, the code in the 1st block is executed and
# no other tests are performed. If the 1st test is false and there is an elif statement next
# the elif (else if) test is performed, if true, the code in the elif block is executed, if False,
# the process continues until you reach else. else is not a test and is run if all other tests
# are false
if cars > people:
	print("We should take the cars.")
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decice.")

if trucks > cars:
	print("That's too many trucks.")
elif trucks < cars:
	print("Maybe we could take the trucks.")
else:
	print("We still can't decide.")

if people > trucks:
	print("Alright, let's just take the trucks.")
else:
	print("Fine, let's stay home then.")