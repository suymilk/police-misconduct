from __future__ import print_function
import fileinput
import csv
import pdb

writer = csv.writer(open("2012sustaineddata.csv", "w"))
writer.writerow(["Log #", "Date of complaint filing", "Incident date", "Location", "Allegations", "Conclusions", "Recommendations"])

# Declare which file to work with
filename = raw_input("Enter filename with extension: ")

with open(filename, "r+") as f:
	data = f.read()
	f.seek(0)
	f.write(" ".join(line.strip() for line in f))

# f = open(filename, "r")
# data = f.read()
# paragraphs = data.split("\n\n")
# print (paragraphs)

# Removing unwanted phrases from document for cleanup
# phrases = []
# phrases.extend(raw_input("Enter the phrases you want to get rid of, separated by commas: ").split(","))
# print (phrases)

# for phrase in phrases:
# 	for line in fileinput.input(filename, inplace=True):
# 		if phrase in line:
# 			continue
# 		print(line, end="")

