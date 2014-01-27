#!/usr/bin/env python
import random, string, sys

key_length = str(sys.argv[1])

alphabet = []
alphabet2 = []
symbols = []
passkey = []
YES_NO = ["yes", "y", "no", "n"]

for char in string.ascii_lowercase:
	alphabet.append(char)
for char in string.ascii_uppercase:
	alphabet2.append(char)
for char in string.punctuation:
	symbols.append(char)

def generate_passkey(key_length):
	"""Generates a random passkey with a length equal to the "key_length" arg"""
	value_invalid = True
	if int(key_length) < 14:
		print "WARNING:"
		print "Cannot guarantee a secure password with so few characters."
		print "Please consider running again with at least 14 characters.\n"
		proceed = raw_input("Proceed? Y/N: ")
		if proceed.lower() not in YES_NO:
			print "\nExiting"
		else:
			if proceed[0].lower() == "y":
				print "Proceeding. Please be aware that passkey may not be secure\n"
			else:
				print "Exiting. Please run again with 14 or more characters"
				value_invalid = False
	while value_invalid == True:
		passkey_length = key_length
		#check integer selected
		try:
			val = int(passkey_length)
			value_invalid = False
		except ValueError:
			print "Not a number, please use format './filename.py {length of key}",
			print "e.g. './keygen.py 16' for a 16 digit key"
			value_invalid = True
			
		if value_invalid == True:
			sys.exit(0)
		else:
			for each in range(0, int(passkey_length)):
				random_number = random.randint(0,4)
				if random_number == 0:
					passkey.append(alphabet[random.randint(0,25)])
				if random_number == 1:
					passkey.append(alphabet2[random.randint(0,25)])
				if random_number == 2:
					passkey.append(str(random.randint(0,9)))
				if random_number == 3:
					passkey.append(symbols[random.randint(0, 31)])

			print "".join(passkey)
	else:
		sys.exit(0)

generate_passkey(key_length)
