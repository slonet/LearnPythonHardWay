# create a mapping of state to abbreviaton
# dictionaries hold key:value pairs. They are not ordered like lists. They form mappings
# between keys and values

# dictionary with keys that are full names of states. The values are the abbreviations.
# dicts are declared with curly braces and a colon between the key and the value
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
# dictionary with keys that are abbreviations and values that are cities.
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
# add key value pairs to the cities dictionary
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
# prints out the values at these specific keys.
# print the values associated with the 'NY' and 'OR' keys in the cities dictionary
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
# print the values associated with the 'Michigan' and 'Florida' keys
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
# gets the value associated with the keys 'Michigan' and 'Florida' from the states dict 
# which happen to also be keys in cities dict.
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
# list(states.items()) returns all the keys and values in a dict as a list. 
# [('key', 'value'), ('key', 'value')...]. the list is iterable and you can make a for loop
# over it
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")

# print every city in state
# same as above
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")

# now do both at the same time
# combining two concepts to iterate over states and get the keys out for cities
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation that might not be there
# if a key is not present, the get() function will return None. None evaluates to False.
state = states.get('Texas')

if not state:
	print("Sorry, no Texas")

# get a city with a different value
# get can accept two arguments. the 2nd argument is what to return (other than None) if the 
# key does not exist
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

""" More dictionary methods
clear()			removes all elements from a dict
copy()			returns a copy of the whole dict
fromkeys()		returns another dict with the specified key value pairs
keys()			returns a list containing the keys
pop()			removes the specified element and returns it
popitem()		removes the last inserted key value pair
setdefault()	returns the value of the specified key, if it does not exist, the key and value are inserted
update()		adds key value pairs to the dict. Can be used to merge dicts.
values()		returns a list of values from the dict.
"""