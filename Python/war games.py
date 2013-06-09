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
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, 
# Boston, MA  02110-1301, USA.
#
# Usage: This prints characters from a given string to the screen,
# one at a time
# It's supposed to look like a 1980's *nix terminal output, like the
# supercomputer from WarGames for example

import time
from sys import stdout

def film_print(string):
    for each in string:
        stdout.write(each)
        stdout.flush()
        time.sleep(0.1)
    print "\n"


# Example usage
# Uncomment the following lines and run this program in a terminal to
# see what the output looks like
#
#film_print("Hello Joshua.")
#time.sleep(3)
#film_print("Would you like to play a game?")

