import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
	line = language_file.readline()

	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)


""" Things I've never seen before
- function inside a return statement (recursion?)
- string.strip()
	- removes any leading or trailing white space from a string
- encode()
- decode()
- using open() with a specific encoding scheme
"""