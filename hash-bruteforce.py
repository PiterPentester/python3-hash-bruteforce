#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python3 hash brute-force
# Copyright (C) 2016 Manuel Brausch

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see: http://www.gnu.org/licenses/

import hashlib, sys
from string import *

stringToBeCracked = "f0e4c2f76c58916ec258f246851bea091d14d4247a2fc3e18694461b1816e13b"
# For possible methods see the generateHashFromString() function 
hashMethod = "sha256"

# Options available for string_list are (for example):
# ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits = '0123456789'
# hexdigits = '0123456789abcdefABCDEF'
# octdigits = '01234567'
# printable = '0123456789abcdefghijklmnopqrstuvwxyzAB...'
# whitespace = ' \t\n\r\x0b\x0c'

string_list = ascii_letters

def generateHashFromString(hashMethod, cleartextString):
	if hashMethod == "md5":
		return hashlib.md5(cleartextString.encode()).hexdigest()
	
	elif hashMethod == "sha1":
		return hashlib.sha1(cleartextString.encode()).hexdigest()
	
	elif hashMethod == "sha224":
		return hashlib.sha224(cleartextString.encode()).hexdigest()
	
	elif hashMethod == "sha256":
		return hashlib.sha256(cleartextString.encode()).hexdigest()
	
	elif hashMethod == "sha384":
		return hashlib.sha384(cleartextString.encode()).hexdigest()
	
	elif hashMethod == "sha512":
		return hashlib.sha512(cleartextString.encode()).hexdigest()
	else:
		pass

def reverseString(string):
	return string[::-1]

def IndexErrorCheck(index_input):
    if len(string_list) <= index_input:
        pass
    else:
        return string_list[index_input]

def StringGenerator(string):
    if len(string) <= 0:
        string.append(string_list[0])
    else:
        # error checking needs to be done, otherwise a ValueError will raise
        string[0] = IndexErrorCheck((string_list.index(string[0]) + 1) % len(string_list))
        if string_list.index(string[0]) == 0:
            return [string[0]] + StringGenerator(string[1:])
    return string

def main():
	generated_string = []
	
	while True:
		generated_string = StringGenerator(generated_string)
		formatted_string = reverseString("".join(generated_string))
		
		if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
			print("Decrypted hash: {}".format(formatted_string))
			sys.exit()

if __name__ == "__main__":
	main()