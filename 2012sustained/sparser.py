from __future__ import print_function
import fileinput

filename = "sustained012012.txt"
phrase = "Created by INDEPENDENT POLICE REVIEW AUTHORITY"

for line in fileinput.input(filename, inplace=True):
	if phrase in line:
		continue
	print(line, end="")