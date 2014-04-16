from __future__ import print_function
import fileinput

phrases = []
filename = "sustained012012.txt"
phrases.extend(raw_input("Enter the phrases you want to get rid of, separated by commas: ").split(", "))
print (phrases)

for phrase in phrases:
	for line in fileinput.input(filename, inplace=True):
		if phrase in line:
			continue
		print(line, end="")