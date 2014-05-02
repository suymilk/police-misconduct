import re
from datetime import datetime
from time import strftime
import itertools

filename = ("sustained012012.txt")

remove_words = ["Created by INDEPENDENT POLICE REVIEW AUTHORITY", "Abstracts of Sustained Cases", "JANUARY 2012", "Page"]

with open(filename) as oldfile, open ('newfile.txt', 'w') as newfile:
	for line in oldfile:
		if not any(remove_word in line for remove_word in remove_words):
			newfile.write(line)

f = open("newfile.txt")

content = str(f.read())

# split file by each incident (starts with "Log")
content = re.split("\n(?=Log)", content)

allcontent = []

# join line breaks caused by pdftotext
allcontent = [log.replace("\n", " ") for log in content]

# all files start with unncessary title that gets grouped into own element; delete element
del allcontent[0]

o = open("out.txt", "w")
print >>o, allcontent

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
for log in allcontent:
	if re.match(r"(\d+)\D+ District", log) == False:
		district = "none"
	else:
		district.append(re.findall(r"(\d+)\D+ District", log))
# print district

# find reference names of officers involved
officers = []
for log in allcontent:
	if "involving" in log:
		if "Officers" in log:
			officers.append(re.findall(r"for\s(Officer\s[A-Z])", log))
		else: 
			officers.append(re.findall(r"(?:\(([A-Z][a-z]+\s[A-Z]))\)", log))
	else:
		officers.append(re.findall(r"CPD\)\s(\w+)", log))
# print officers  

# split allcontent into sentences to allow iterating by sentences

bysentence = []

for log in allcontent:
	bysentence.append(re.split("[.!?][\s]{1,2}(?=[A-Z])", log))
	# print bysentence

for sentence in bysentence:
	# print sentence
	recs = []
	for thing in sentence:
		if "IPRA recommended" in thing:
			recs.append(thing)
	print recs




# what are the recommendations?
# for log in allcontent:
# 	rec = re.findall(f")
# 	look for content between "" \\(xe2)\\(x80)\\(x9c).+?\\(xe2)\\(x80)\\(x9d)


# pattern for the evidence used in coming to a conclusion? "Based on x, x, x"


# find how long it took IPRA to come to a conclusion on a complaint (convert complaint file date to string (strptime), subtract from converted date of file name to datetime object)