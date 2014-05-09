import re, glob, os, sys, itertools, sys
from collections import Counter

remove_words = ["Created by INDEPENDENT POLICE REVIEW AUTHORITY", "Abstracts of Sustained Cases", "2012", "Page"]

read_files = glob.glob("*.txt")

input = "2012sustainedALL.txt"
output = "2012sustainedCLEAN.txt"

with open(input, "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

fIn = open(input)
fOut = open(output, "w")

for line in fIn:
	if not True in [word in line for word in remove_words]:
		fOut.write(line)

content = open(output, "r")
content = str(content.read())

# split file by each incident (starts with "Log")
content = re.split("\n(?=Log)", content)

allcontent = []

# join line breaks caused by pdftotext
allcontent = [log.replace("\n", " ") for log in content]

# all files start with unncessary title that gets grouped into own element; delete element
del allcontent[0]

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
	district.append(re.findall(r"(\d+)\D+ District", log))

district = list(itertools.chain.from_iterable(district))
print district
print Counter(district)