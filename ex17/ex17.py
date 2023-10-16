from sys import argv
# exists will return a boolean indicating whether or not a file in question exists
from os.path import exists

script, from_file, to_file = argv


indata = open(from_file).read()
print(f"Copying {len(indata)} bytes from {from_file} to {to_file}")

if(exists(to_file)):
	out_file = open(to_file, 'w')
	out_file.write(indata)
	out_file.close()
else:
	print(f"The output file does not exist. Aborting.")