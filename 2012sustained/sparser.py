import re
from datetime import datetime
from time import strftime

filename = ("sustained012012.txt")
f = open(filename)
content = str(f.read())

# get digits (date of publication of investigations) from filename
# pblstr = filter(str.isdigit, filename)
# pbl = datetime(year=int(pblstr[2:5]), month=int(pblstr[0:1]))
# print pbl

# split file by each incident (starts with "Log")
content = re.split("\n(?=Log)", content)
# print content

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
	# if re.match(r"(\d+)\D+ District", log) == False:
	# 	district[log] = "none"
	# else:
	district = re.findall(r"(\d+)\D+ District", log)
	# print district

# find reference names of officers involved
for log in allcontent:
	if "involving" in log:
		if "Officers" in log:
			officers = re.findall(r"for\s(Officer\s[A-Z])", log)
			print officers
		else: 
			officers = re.findall(r"(?:\(([A-Z][a-z]+\s[A-Z]))\)", log)
			print officers		
	else:
		officers = re.findall(r"CPD\)\s(\w+)", log)
		print officers  




# what are the recommendations?
# for log in allcontent:
# 	rec = re.findall(f")
# 	look for content between "" \\(xe2)\\(x80)\\(x9c).+?\\(xe2)\\(x80)\\(x9d)

# pattern for looking for officers involved: if only one, no parentheses to indicate officer A or officer B, etc. if more than one, reference names are set off by parentheses. in parentheses, the type of officer is referenced (i.e. sergeant, officer, lieutenant); do we want that? potential categories: type of officers involved, number of officers involved, reference names of officers involved

# pattern for the evidence used in coming to a conclusion? "Based on x, x, x"

# pattern for allegations "It was alleged that " skip over noun, go to verb? NLTK?

# find how long it took IPRA to come to a conclusion on a complaint (convert complaint file date to string (strptime), subtract from converted date of file name to datetime object)

