#/usr/bin/env python
def milesToKm(miles):
	return float(miles) * 1.609344
def kmToMiles(km):
	return float(km) * 0.621371
answer = ""	
while answer != "q":
	print "Type q to quit."
	print "Select 1 to convert miles to km"
	print "Select 2 to convert km to miles"
	answer = raw_input("")
	if answer == "1":
		miles = raw_input("How many miles is it? ")
		print "That's " + str(milesToKm(miles)) + " km!"
	elif answer == "2":
		km = raw_input("How many km is it? ")
		print "That's " + str(kmToMiles(km)) + " miles!"
	elif answer == "q":
		break
	else: print "Sorry, I don't understand that command"
