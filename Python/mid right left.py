#!/usr/bin/env python
# Program written by Paul Lenton (EckoZero) - <lentonp@gmail.com>
# Copyright 2013
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the 
#Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, 
#Boston, MA  02110-1301, USA.

# A quick note on usage:
# 
# This program was written as a replacement for string slice commands using
# the [n:n:n] native to Python. It was originally a learning project.
#
# To use any of these string slicers, import this module to your program,
# then use 
# print function_name(String-to-be-sliced, arg1, arg2 (if required)

def mid(strInput, start, length=1):
	strOutput = []
	midOutput = []
	#as lists start at 0 and the input will not expect this, reduce the
	#numerical value of start by 1 to keep in line with lists
	start -= 1
	#break string into a list to count through later
	for letters in strInput:
		strOutput.append(letters)
	#check whether or not the inputs are all valid
	if start < 0:
		z = "You can't use negative numbers for this. Consider "
		z1 = "using the 'right' function instead."
		return z + z1
	elif start > len(strInput):
		a = "Your start number is further than the last letter in the string. \n"
		b = "Please try a different start point."
		return a + b
	else:
		count = 0
		while count != length:
			midOutput.append(strOutput[start])
			start += 1
			count += 1
		return "".join(midOutput)


def left(strInput, length):
	strOutput =[]
	leftOutput = []
	#assign start variable as this will need to be used later
	start = 0
	#drop letters into string to count along them later on
	for letter in strInput:
		strOutput.append(letter)
	#check inputs are valid
	if length < 0:
		return "You can't use negative numbers for this"
	elif length > len(strInput):
		return "Your 'length' input is longer than your string input!"
	else:
		count = 0
		while count != length:
			leftOutput.append(strOutput[start])
			count += 1
			start += 1
		return "".join(leftOutput)

print left("Fit like a prostitute", 7)

def right(strInput, length):
	#most ambitious one yet as I need to go through this backwards!
	strOutput = []
	rightOutput =[]
	start = len(strInput)
	for letter in strInput:
		strOutput.append(letter)
	#again, check the validity of the inputs
	if length < 0:
		a = "Sorry, you have to use a positive number here. It will "
		b = "already go through the list starting at the right."
		return a + b
	elif length > start:
		return "There aren't that many letters in the string."
	else:
		count = 0
		start2 = start - length
		while start2 != start:
			while count != length:
				rightOutput.append(strOutput[start2])
				count += 1
				start2 += 1
		return "".join(rightOutput)

