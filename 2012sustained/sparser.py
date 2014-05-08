import re, glob, os, sys, itertools
from collections import Counter

for file in glob.glob("*.txt"):
	with open(file) as content:
		content = content.read()

# remove_words = ["Created by INDEPENDENT POLICE REVIEW AUTHORITY", "Abstracts of Sustained Cases", "2012", "Page"]

# with open(filename) as oldfile, open ('newfile.txt', 'w') as newfile:
# 	for line in oldfile:
# 		if not any(remove_word in line for remove_word in remove_words):
# 			newfile.write(line)

# f = open("newfile.txt")

# split file by each incident (starts with "Log")
	content = re.split("\n(?=Log)", content)

	allcontent = []

	# join line breaks caused by pdftotext
	allcontent = [log.replace("\n", " ") for log in content]

	# all files start with unncessary title that gets grouped into own element; delete element
	del allcontent[0]

	# what's this thing look like?
	# o = open("out.txt", "w")
	# print >>o, allcontent

	# find all Log/C.R. numbers, store to logno
	for log in allcontent:
		logno = re.findall(r"No. (\d+)", log)
		# print logno

	# find all dates on which the complaint was filed
	for log in allcontent: 
		datefiled = re.findall(r"\d+\sOn\s([A-z]+\s\d+,\s\d+)", log)
		# print datefiled

	# find the district in which the incident occurred
	district = []
	alldistrict = []
	for log in allcontent:
		district.append(re.findall(r"(\d+)\D+ District", log))

	# district = list(itertools.chain.from_iterable(district))
	print district
	# print Counter(alldistrict)

