import re

f = open("sustained012012.txt")
content = str(f.read())

content = re.split("\n(?=Log)", content)
# print content

# mycontent = map(lambda each:each.strip("\n"), content)

allcontent = []

allcontent = [log.replace("\n", " ") for log in content]


o = open("out.txt", "w")
print >>o, allcontent

# find all Log/C.R. numbers, store to logno
for log in allcontent:
	logno = re.findall(r"No. (\d+)", log)
	# print logno

for log in allcontent: 
	datefiled = re.findall(r"\d+\sOn\s([A-z]+\s\d+,\s\d+)", log)
	print datefiled


