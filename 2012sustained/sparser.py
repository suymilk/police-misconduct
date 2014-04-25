import re

f = open("sustained012012.txt")
content = str(f.read())

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
	print district

# pattern for looking for officers involved: if only one, no parentheses to indicate officer A or officer B, etc. if more than one, reference names are set off by parentheses. in parentheses, the type of officer is referenced (i.e. sergeant, officer, lieutenant); do we want that? potential categories: type of officers involved, number of officers involved, reference names of officers involved

# pattern for the evidence used in coming to a conclusion? "Based on x, x, x"

# pattern for allegations "It was alleged that " skip over noun, go to verb? NLTK?

