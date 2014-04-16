from __future__ import print_function
import fileinput
import pdb

phrases = []
filename = raw_input("Enter filename with extension: ")

phrases.extend(raw_input("Enter the phrases you want to get rid of, separated by double commas: ").split(",,"))
# for phrase in phrases:
# 	phrases = phrase.lower()
print (phrases)

for phrase in phrases:
	for line in fileinput.input(filename, inplace=True):
		# line = line.lower()
		if phrase in line:
			continue
		print(line, end="")